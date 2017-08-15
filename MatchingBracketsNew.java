import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * There is still some debugging left to do apparently because this returned the wrong
* answer to hidden test cases given on hackerrank.com
* however it returns the right answer on all test cases i can think of 
* or randomly generate so I’m gonna come back and keep testing
 */

public class MatchingBracketsNew {
    
    /*static String isBalanced(String s) {
        
    }*/
    /*
     helper functions needed:
     find_concentric_clusters 
     returns a list of all concentric clusters
     first finds matching bracket pairs that are right next to each other
     (e.g. "()" and "[]" in }[]{()" )
     then looks left and right of each (if possible) to see if they are directly enclosed by another matching pair
     (e.g. ""{()}" in ][}{()}" )
     combine_clusters
     NOTE: a cluster is denoted by the ordered pair {leftmost_idx,rightmost_idx}
     works by checking if there are any concentric clusters next to each other
     and combines them if they are directly enclosed by a matching pair
     (e.g. "()" and "{}" are combined to make "[(){}]" in "{()][[(){}]" )
     returns a list of all clusters after they have been combined as much as possible
     */ 
    public static ArrayList<int[]> find_concentric_clusters(String s) {
        char[] s_chars = s.toCharArray();
        String curly = "{}";
        char curly_o = curly.charAt(0);
        char curly_c = curly.charAt(1);
        String square = "[]";
        char square_o = square.charAt(0);
        char square_c = square.charAt(1);
        String round = "()";
        char round_o = round.charAt(0);
        char round_c = round.charAt(1);
        ArrayList<int[]> concentric_clusters = new ArrayList<int[]>();
        for (int i = 0; i < s_chars.length-1; i++) {
            switch (s_chars[i]) {
                case '{':
                    if (s_chars[i+1] == '}') {
                        int[] pair_to_add = {i,i+1};
                        concentric_clusters.add(pair_to_add);
                    }
                    break;
                case '[':
                    if (s_chars[i+1] == ']') {
                        int[] pair_to_add = {i,i+1};
                        concentric_clusters.add(pair_to_add);
                    }
                    break;
                case '(':
                    if (s_chars[i+1] == ')') {
                        int[] pair_to_add = {i,i+1};
                        concentric_clusters.add(pair_to_add);
                    }
                    break;
            }
        }
        //now have pairs of matching brackets right next to each other
        //try to expand to see if have larger concentric clusters
        for (int i = 0; i < concentric_clusters.size(); i++) {
            int leftmost = concentric_clusters.get(i)[0];
            int rightmost = concentric_clusters.get(i)[1];
            int lefter = leftmost - 1;
            int righter = rightmost + 1;
            boolean stop = false;
            while (((lefter > -1) && (righter < s_chars.length)) && (stop == false)) {
                //were still on the grid
                //check if these are a matching pair
                switch (s_chars[lefter]) {
                    case '{':
                        if (s_chars[righter] == '}') {
                            int[] corrected_cluster = {lefter,righter};
                            concentric_clusters.set(i,corrected_cluster);
                        }
                        else {
                            stop = true;
                        }
                        break;
                    case '[':
                        if (s_chars[righter] == ']') {
                            int[] corrected_cluster = {lefter,righter};
                            concentric_clusters.set(i,corrected_cluster);
                        }
                        else {
                            stop = true;
                        }
                        break;
                    case '(':
                        if (s_chars[righter] == ')') {
                            int[] corrected_cluster = {lefter,righter};
                            concentric_clusters.set(i,corrected_cluster);
                        }
                        else {
                            stop = true;
                        }
                        break;
                        
                    default:
                        stop = true;
                
                }
                lefter = lefter - 1;
                righter = righter + 1;
            }
        }
        return concentric_clusters;
        
    }
    
    public static ArrayList<int[]> combine_clusters(String s, ArrayList<int[]> concentric_clusters) {
        ArrayList<int[]> ret = new ArrayList<int[]>();
        for (int i = 0; i < concentric_clusters.size(); i++) {
            //System.out.println("int i:");
            //System.out.println(i);
            //we are iterating through the clusters
            //keep adding clusters to itm_to_add_to_list_of_consecutive_clusters as they are found
            char[] s_chars = s.toCharArray();
            ArrayList<int[]> itm_to_add_to_list_of_consecutive_clusters = new ArrayList<int[]>();
            itm_to_add_to_list_of_consecutive_clusters.add(concentric_clusters.get(i));
            int leftmost_idx = concentric_clusters.get(i)[0];
            int rightmost_idx = concentric_clusters.get(i)[1];
            //if this cluster is already in one of combined clusters we've done, skip it
            boolean skip = false;
            if ((ret.size() > 0) && (cluster_contained_in_some_cluster(ret, leftmost_idx, rightmost_idx))) {
                skip = true;
            }
            boolean found = false;
            boolean start = true;
            int count = 0;
            //take out the count once figure out what is wrong
            while ((((found == true) || (count == 0))&& (count < 100))&&(skip == false)) {
                //System.out.println("a");
                //System.out.println("found: ");
                //System.out.println(found);
                start = false;
                //System.out.println("count:");
                //System.out.println(count);
                int j_start = i+1;
                found = false;
                for (int j = j_start; j < concentric_clusters.size(); j++) {
                    //System.out.println("b");
                    //System.out.println("i:");
                    //System.out.println(i);
                    //System.out.println("j:");
                    //System.out.println(j);
                    //System.out.println("j_start:");
                    //System.out.println(j_start);
                    //System.out.println("rightmost_idx:");
                    //System.out.println(rightmost_idx);
                    
                    if (concentric_clusters.get(j)[0] == rightmost_idx + 1) {
                        //System.out.println("jth concentric cluster:");
                        //print_elts_in_int_list(concentric_clusters.get(j));
                        //System.out.println("found");
                        
                        found = true;
                        itm_to_add_to_list_of_consecutive_clusters.add(concentric_clusters.get(j));
                        
                        rightmost_idx = concentric_clusters.get(j)[1];
                        j_start = j + 1;
                        //System.out.println("c");
                        
                    }
                    else {
                         //System.out.println("not found");
                         //found = false;
                    }
                    //System.out.println();
                }
                count = count + 1;
            }
            //if item_to_left matches item_to_right
            boolean left_and_right_match = false;
            int idx_to_left = itm_to_add_to_list_of_consecutive_clusters.get(0)[0]-1;
            int idx_to_right = itm_to_add_to_list_of_consecutive_clusters.get(itm_to_add_to_list_of_consecutive_clusters.size() - 1)[1]+1;
            if (((idx_to_left > -1) && (idx_to_right < s_chars.length))&&(skip == false)) {
                //System.out.println("d");
                char itm_to_left = s_chars[idx_to_left];
                char itm_to_right = s_chars[idx_to_right];
                
                switch (itm_to_left) {
                    case '{':
                        //System.out.println("e");
                        if (itm_to_right == '}') {
                            left_and_right_match = true;
                        }
                        break;
                    case '[':
                        //System.out.println("f");
                        if (itm_to_right == ']') {
                            left_and_right_match = true;
                        }
                        break;
                    case '(':
                        //System.out.println("g");
                        if (itm_to_right == ')') {
                            left_and_right_match = true;
                        }
                        break;
                    default:
                        //System.out.println("h");
                        break;
                }
            }
            if (skip == false) {
                if (left_and_right_match) {
                    //System.out.println("l");
                    int[] cluster_left_right_idxs = {idx_to_left,idx_to_right};
                    ret.add(cluster_left_right_idxs);
                }
                else {
                    //System.out.println("m");
                    //for each elt of itm_to_add_to_list_of_consecutive_clusters
                    //add it to ret
                    for (int k = 0; k < itm_to_add_to_list_of_consecutive_clusters.size(); k++) {
                        ret.add(itm_to_add_to_list_of_consecutive_clusters.get(k));
                    }
                }
            }
        }
        return ret;
    }
    
    public static ArrayList<int[]> completely_combine_clusters(String s, ArrayList<int[]> clusters) {
        ArrayList<int[]> feed_in = clusters;
        boolean combined = true;
        while (combined == true) {
            combined = false;
            ArrayList<int[]> fed_in = feed_in;
            //print_elts_array_int_list(fed_in); 
            feed_in = combine_clusters(s, feed_in);
            //print_elts_array_int_list(feed_in);
            //System.out.println();
            if (fed_in.size() != feed_in.size()) {
                combined = true;
            }
        }
        return feed_in;
    }
        public static ArrayList<String> generate_bracket_test_cases(int n) {
        //n is the number of strings
        HashMap<Integer,Character> int_to_brace = new HashMap<Integer,Character>();
        int_to_brace.put(6,'{');
        int_to_brace.put(1,'}');
        int_to_brace.put(2,'[');
        int_to_brace.put(3,']');
        int_to_brace.put(4,'(');
        int_to_brace.put(5,')');
        
        ArrayList<String> ret = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            int len_str = (int)(Math.floor(Math.random() * 50 + 1));
            String str = "";
            for (int j = 0; j < len_str; j++) {
                int int_to_add = (int)(Math.floor(Math.random()*6+1));
                char char_to_add = int_to_brace.get(int_to_add);
                String string_to_add = String.valueOf(char_to_add);
                str = str + string_to_add;
            }
            ret.add(str); 
        }
        return ret;
    }
    
    public static void print_array_list_string(ArrayList<String> listy) {
        for (int i = 0; i < listy.size(); i++) {
            System.out.println(listy.get(i));
        }
    }
    
    
    public static boolean cluster_contained_in_some_cluster(ArrayList<int[]> clusters, int leftmost_idx, int rightmost_idx) {
        boolean ret = false;
        for (int i = 0; i < clusters.size(); i++) {
            int cluster_left = clusters.get(i)[0];
            int cluster_right = clusters.get(i)[1];
            if ((leftmost_idx >= cluster_left) && (rightmost_idx <= cluster_right)) {
                ret = true;
                return true;
            }
        }
        return ret;
            
    }
    
    static String isBalanced(String s) {
        ArrayList<int[]> concentric_clusters = find_concentric_clusters(s);
        ArrayList<int[]> combined_clusters = completely_combine_clusters(s, concentric_clusters);
        boolean ret = all_indices_contained_in_some_cluster(s, combined_clusters);
        if (ret == true) {
            return "YES";
        }
        else {
            return "NO";
        }
    }
    
    public static boolean idx_contained_in_cluster(int idx, int[] cluster) {
        int lower = cluster[0];
        int higher = cluster[1];
        if ((idx >= lower) && (idx <= higher)) {
            return true;
        }
        else {
            return false;
        }
    }
    
    public static boolean all_indices_contained_in_some_cluster(String s, ArrayList<int[]> clusters) {
        char[] s_chars = s.toCharArray();
        int len_s = s_chars.length;
        boolean[] idxs_contained = new boolean[len_s];
        for (int i = 0; i < len_s; i++) {
            boolean idx_in_cluster = false;
            for (int j = 0; j < clusters.size(); j++) {
                if (idx_contained_in_cluster(i,clusters.get(j))) {
                    idx_in_cluster = true;
                }
            }
            idxs_contained[i] = idx_in_cluster;
        }
        boolean all_idxs_contained = true;
        for (int i = 0; i < len_s; i++) {
            if (idxs_contained[i] == false) {
                all_idxs_contained = false;
                break;
            }
        }
        return all_idxs_contained;
        
    }
    
    public static boolean lists_have_no_common_elts(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        if (list1.size() == 0 || list2.size() == 0) {
            return true;
        } 
        for (int i = 0; i < list1.size(); i++) {
            for (int j = 0; j < list2.size(); j++){
                if (list1.get(i) == list2.get(j)) {
                    ////System.out.println("h");
                    return false;
                }
            }
        }
        return true;
    }
    
    public static void print_elts_array_int_list(ArrayList<int[]> opening_and_closing_idxs) {
        String print_itm = "{";
        if (opening_and_closing_idxs.size() == 0) {
            print_itm = print_itm + "}";
        }
        else {
            for (int i = 0; i < opening_and_closing_idxs.size()-1; i++) {
                print_itm = print_itm + "{" + opening_and_closing_idxs.get(i)[0] + ", " + opening_and_closing_idxs.get(i)[1] + "}" + ", ";
            }
            print_itm = print_itm + "{" + opening_and_closing_idxs.get(opening_and_closing_idxs.size()-1)[0] + ", " + opening_and_closing_idxs.get(opening_and_closing_idxs.size()-1)[1] + "}" + "}";
        }
        System.out.println(print_itm);
    }
    
    public static void print_elts_in_int_list(int[] opening_and_closing_idx) {
        String print_itm = "{";
        for (int i = 0; i < opening_and_closing_idx.length-1; i++) {
            print_itm = print_itm + opening_and_closing_idx[i] + ", ";
        }
        print_itm = print_itm + opening_and_closing_idx[opening_and_closing_idx.length-1] + "}";
        System.out.println(print_itm);
    }
    
    public static void main(String[] args) {
        /*Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            String s = in.next();
            String result = isBalanced(s);
            System.out.println(result);
        }
        in.close(); */
        String string1 = "}[]{()";
        /*
        System.out.println("Below should print {{1,2},{4,5}}.");*/
        String string2 = "][}{()}";
        /*
        ArrayList<int[]> ret1 = find_concentric_clusters(string1);
        print_elts_array_int_list(ret1);
        System.out.println();
        System.out.println("Below should print {{3,6}}.");
        ArrayList<int[]> ret2 = find_concentric_clusters(string2);
        print_elts_array_int_list(ret2);
        System.out.println();*/
        
        String string3 = "{()][[(){}]";
        /*
        ArrayList<int[]> concentric_clusters3 = find_concentric_clusters(string3);
        System.out.println("concentric_clusters3:");
        print_elts_array_int_list(concentric_clusters3);
        System.out.println("Below should print {{1,2},{5,10}}.");
        ArrayList<int[]> ret3 = combine_clusters(string3, concentric_clusters3);
        print_elts_array_int_list(ret3);*/
        
        String string4 = "{()][[(){}[]][(){}]}";
        /*
        ArrayList<int[]> concentric_clusters4 = find_concentric_clusters(string4);
        System.out.println("concentric_clusters4:");
        print_elts_array_int_list(concentric_clusters4);
        System.out.println("Below should print {{1,2}{5,12},{13,18}}.");
        ArrayList<int[]> ret4 = completely_combine_clusters(string4, concentric_clusters4);
        print_elts_array_int_list(ret4);*/
        
        String string5 = "{[()]}";
        /*
        ArrayList<int[]> concentric_clusters5 = find_concentric_clusters(string5);
        System.out.println("concentric_clusters5:");
        print_elts_array_int_list(concentric_clusters5);
        System.out.println("Below should print {{0,5}}.");
        ArrayList<int[]> ret5 = completely_combine_clusters(string5, concentric_clusters5);
        print_elts_array_int_list(ret5);*/
        
        String string6 = ")({]][()[]{){](){}}({}{})}({{{())";
        /*ArrayList<int[]> concentric_clusters6 = find_concentric_clusters(string6);
        System.out.println("concentric_clusters6:");
        print_elts_array_int_list(concentric_clusters6);
        System.out.println("completely combined clusters:");
        ArrayList<int[]> ret6 = completely_combine_clusters(string6, concentric_clusters6);
        print_elts_array_int_list(ret6);*/
        
        String string7 = "{()[]()[]()[]}";
        String string8 = "{{[[(())]]}}";
        
        System.out.println("Below should print:");
        System.out.println("1: NO");
        System.out.println("2: NO");
        System.out.println("3: NO");
        System.out.println("4: NO");
        System.out.println("5: YES");
        System.out.println("6: NO");
        System.out.println("7: YES");
        System.out.println("8: YES");
        System.out.println();
        
        System.out.print("1: ");
        System.out.println(isBalanced(string1));
        System.out.print("2: ");
        System.out.println(isBalanced(string2));
        System.out.print("3: ");
        System.out.println(isBalanced(string3));
        System.out.print("4: ");
        System.out.println(isBalanced(string4));
        System.out.print("5: ");
        System.out.println(isBalanced(string5));
        System.out.print("6: ");
        System.out.println(isBalanced(string6));
        System.out.print("7: ");
        System.out.println(isBalanced(string7));
        System.out.print("8: ");
        System.out.println(isBalanced(string8));
        
        ArrayList<String> test_cases = generate_bracket_test_cases(20);
        for (int i = 0; i < 20; i++) {
            String test_case = test_cases.get(i);
            System.out.println("test case " + i + ":");
            System.out.println(test_case);
            ArrayList<int[]> concentric_clusters = find_concentric_clusters(test_case);
            System.out.println("concentric_clusters:");
            print_elts_array_int_list(concentric_clusters);
            System.out.println("completely combined clusters:");
            ArrayList<int[]> ret = completely_combine_clusters(test_case, concentric_clusters);
            print_elts_array_int_list(ret);
            System.out.print("balanced:? ");
            System.out.println(isBalanced(test_case));
            System.out.println();
            
        }

    }
}
