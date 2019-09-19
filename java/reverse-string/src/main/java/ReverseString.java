class ReverseString {

    String reverse(String inputString) {
        StringBuilder newString = new StringBuilder(inputString);
        newString.reverse();
        return newString.toString();
    }
}
