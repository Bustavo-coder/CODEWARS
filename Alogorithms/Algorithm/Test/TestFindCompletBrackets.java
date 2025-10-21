import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TestFindCompletBrackets {
    @Test
    @DisplayName("TEST CORRECT Name")
    public void testFunctionCorect(){
        FindCompleteBrackets findCompleteBrackets = new FindCompleteBrackets();
        boolean result = findCompleteBrackets.checkWords("()[]{}<>");
        assertTrue(result);
    }
    @Test
    @DisplayName("test for False")
    public void testFunctionFalse(){
        FindCompleteBrackets findCompleteBrackets = new FindCompleteBrackets();
        boolean result = findCompleteBrackets.checkWords("({}");
        assertFalse(result);
    }

}
