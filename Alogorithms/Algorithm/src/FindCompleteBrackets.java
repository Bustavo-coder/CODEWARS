import java.util.ArrayList;

public class FindCompleteBrackets {
   private char[] leftBrackets = {'{', '[', '<', '('};
    private char[] rightBrackets = {'}', ']', '>', ')'};
     private ArrayList<Boolean> occurence = new ArrayList<>();

    public Boolean checkWords(String words) {
        for (int count = 0; count < leftBrackets.length; count++) {
            int leftOccurence = 0;
            int rightOccurence = 0;
            for(int counter = 0; counter < words.length(); counter++) {
                if(words.charAt(counter) == leftBrackets[count]) leftOccurence++;
                if(words.charAt(counter) == rightBrackets[count]) rightOccurence++;
            }
            occurence.add(leftOccurence == rightOccurence);

        }
        System.out.println(occurence);
        return !occurence.contains(false);
    }
}