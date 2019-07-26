class RnaTranscription {

    String transcribe(String dnaStrand) {
        char[] splittedDna = dnaStrand.toCharArray();

        for(int i = 0; i < splittedDna.length; i++) {
            switch(splittedDna[i]) {
                case 'C':
                    splittedDna[i] = 'G';
                    break;
                case 'T':
                    splittedDna[i] = 'A';
                    break;
                case 'G':
                    splittedDna[i] = 'C';
                    break;
                case 'A':
                    splittedDna[i] = 'U';
                    break;
                default:
                    throw new IllegalArgumentException("Invalid input");
            }
        }
        return new String(splittedDna);
    }

}
