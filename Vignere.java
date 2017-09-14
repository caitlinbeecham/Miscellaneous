
import java.util.HashMap;

public class Vignere {
    
    
    public static char[][] GenerateVignereLookUpTable() {
        char[][] ret = new char[26][26];
        char[] alpha_strings = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        int start_idx = 0;
        for (int i = 0; i < 26; i++) {
            char[] line = new char[26];
            int offset = 0;
            for (int j = 0; j < 26; j++) {
                line[j] = alpha_strings[start_idx + offset];
                if (start_idx + offset < 25) { 
                    offset++;
                }
                else {
                    offset = -start_idx;
                }
            }
            ret[start_idx] = line;
            start_idx++;
        }
        return ret;
    }
    
    public static HashMap<Character,Integer> ConstructLetterToIdx() {
        char[] alpha_strings = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        HashMap<Character,Integer> letter_to_idx = new HashMap<Character,Integer>();
        for (int i = 0; i < alpha_strings.length; i++) {
            letter_to_idx.put(alpha_strings[i], i);
        }
        return letter_to_idx;
    }
    
    public static String Encrypt(String plaintext, String key) {
        String ret = "";
        char[] plaintext_char_list = plaintext.toCharArray();
        char[] key_char_list = key.toCharArray();
        int key_idx = 0;
        HashMap<Character,Integer> LetterToIdx = ConstructLetterToIdx();
        char[][] LookUpTable = GenerateVignereLookUpTable();
        for (int i = 0; i < plaintext_char_list.length; i++) {
            char key_letter = key_char_list[key_idx];
            char plaintext_letter = plaintext_char_list[i];
            int key_letter_idx = LetterToIdx.get(key_letter);
            int plaintext_letter_idx = LetterToIdx.get(plaintext_letter);
            char letter_to_add = LookUpTable[key_letter_idx][plaintext_letter_idx];
            ret = ret + letter_to_add;
            if (key_idx < key_char_list.length - 1) {
                key_idx++;
            }
            else {
                key_idx = 0;
            }
        }
        return ret;
    }
    
    //public static String Decrypt(String ciphertext, String key) {
    
    //}
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.out.println(Encrypt("hallelujah","bio"));
        
    }
    
}
