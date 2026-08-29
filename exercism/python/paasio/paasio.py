"""Metered wrappers for file and socket I/O operations."""

import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        """Return this wrapper when entering a context manager."""
        # Keep context behavior local: return wrapper, don't call parent __enter__.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Delegate context cleanup to the wrapped file object."""
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        """Return an iterator over lines from this file."""
        return self

    def __next__(self):
        """Read the next line and update read statistics."""
        line = super().readline()
        self._read_ops += 1
        self._read_bytes += len(line)
        if not line:
            raise StopIteration
        return line

    def read(self, size=-1):
        """Read bytes from the file and update read statistics."""
        data = super().read(size)
        self._read_ops += 1
        self._read_bytes += len(data)
        return data

    @property
    def read_bytes(self):
        """Total number of bytes read from the file."""
        return self._read_bytes

    @property
    def read_ops(self):
        """Total number of read operations performed."""
        return self._read_ops

    def write(self, b):
        """Write bytes to the file and update write statistics."""
        written = super().write(b)
        self._write_ops += 1
        self._write_bytes += written
        return written

    @property
    def write_bytes(self):
        """Total number of bytes written to the file."""
        return self._write_bytes

    @property
    def write_ops(self):
        """Total number of write operations performed."""
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        """Return this wrapper when entering a context manager."""
        # Mirror MeteredFile: return wrapper and delegate only on exit.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Delegate context cleanup to the wrapped socket object."""
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        """Receive bytes and update receive statistics."""
        data = self._socket.recv(bufsize, flags)
        self._recv_ops += 1
        self._recv_bytes += len(data)
        return data

    @property
    def recv_bytes(self):
        """Total number of bytes received from the socket."""
        return self._recv_bytes

    @property
    def recv_ops(self):
        """Total number of recv operations performed."""
        return self._recv_ops

    def send(self, data, flags=0):
        """Send bytes and update send statistics."""
        sent = self._socket.send(data, flags)
        self._send_ops += 1
        self._send_bytes += sent
        return sent

    @property
    def send_bytes(self):
        """Total number of bytes sent to the socket."""
        return self._send_bytes

    @property
    def send_ops(self):
        """Total number of send operations performed."""
        return self._send_ops
