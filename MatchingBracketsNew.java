import java.util.EmptyStackException;
import java.util.*;

public class MatchingBrackets {
	/**
	 * @param args
	 * figured out how to do this never wrote it up, this way is much faster, still need to test some more but seems to work
	 */
	public static boolean is_matched(String brackets) {
		/*
		 * How i will do this:
		 * for char in brackets
		 * push to stack1
		 * while stack 1 is not empty
		 *     then while stack1.peek is a closing bracket
		 *     stack2.push(stack1.pop)
		 *     then while stack1.peek is an opening bracket
		 *         check if stack1.pop and stack2.pop match
		 *         if ever not then return false
		 *         or if stack2 is empty while the above while loop is still running
		 *         return false
		 *         or if the above while loop finishes and stack2 is NOT empty return False
		 */

		String braces = "[({})]";
		Set<Character> opening_brackets = new HashSet<Character>();
		Set<Character> closing_brackets = new HashSet<Character>();
		for (int i = 0; i < 3; i++) {
			opening_brackets.add(braces.charAt(i));
		}
		for (int i = 3; i < 6; i++) {
			closing_brackets.add(braces.charAt(i));
		}
		Stack stack1 = new Stack();
		Stack stack2 = new Stack();
		char[] brackets_chars = brackets.toCharArray();
		for (char c : brackets_chars) {
			stack1.push(c);
		}
		while (!(stack1.is_empty())) {
			char current_char = stack1.peek();
			while ((!(stack1.is_empty())) && (closing_brackets.contains(current_char))) {
				stack2.push(stack1.pop());
				if (!(stack1.is_empty())) {
				    current_char = stack1.peek();
				}
				else {
					break;
				}
			}
		    while ((!(stack1.is_empty())) && (opening_brackets.contains(current_char))) {
		    	if (stack2.is_empty()) {
		    		System.out.println("return false at point a");
		    		return false;
		    	}
		    	char c1 = stack1.pop();
		    	char c2 = stack2.pop();
		    	if (!(matches(c1,c2))) {
		    		System.out.println("c1");
		    		System.out.println(c1);
		    		System.out.println("c2");
		    		System.out.println(c2);
		    		System.out.println("return false at point b");
		    		return false;
		    	}
		    	if (!(stack1.is_empty())) {
		    	    current_char = stack1.peek();
		    	}
		    	else {
		    		break;
		    	}
		    }
		    //if (!(stack2.is_empty())) {
		    	//System.out.println("return false at point c");
		    	//return false;
		    //}	
		}
		if (!(stack2.is_empty())) {
			System.out.println("return false at point d");
	    	return false;
	    }
		return true;
	}
		
	
	public static boolean matches(char opening_bracket, char closing_bracket) {
		if ((opening_bracket == '(') && (closing_bracket == ')')) {
			return true;
		}
		else if ((opening_bracket == '[') && (closing_bracket == ']')) {
			return true;
		}
		else if ((opening_bracket == '{') && (closing_bracket == '}')) {
			return true;
		}
		else {
			return false;
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String braces = "[({})]";
		char test_open = braces.charAt(0);
		char test_close = braces.charAt(5);
		boolean is_match = matches(test_open,test_close);
		System.out.println("should be true");
		System.out.println(is_match);
		String string1 = "[[[[[";
		String string2 = "{}[][]()";
		String string3 = "([{}[]])";
		System.out.println("Should print false");
		System.out.println(is_matched(string1));
		System.out.println("should print true");
		System.out.println(is_matched(string2));
		System.out.println("should print true");
		System.out.println(is_matched(string3));
	}

}

class Stack {
	StackNode top;
	public Stack() {
		this.top = null;
	}
	
	public boolean is_empty() {
		boolean ret = false;
		if (this.top == null) {
			ret = true;
		}
		return ret;
	}
	
	public void push(char data) {
		StackNode new_node = new StackNode(data);
		if (this.is_empty()) {
			this.top = new_node;
		}
		else {
			new_node.next = this.top;
			this.top = new_node;
		}
	}
	
	public char pop() {
		if (this.is_empty()) {
			throw new EmptyStackException();
		}
		else {
			char ret = this.top.data;
			this.top = this.top.next;
			return ret;
		}
	}
	
	public char peek() {
		if (this.is_empty()) {
			throw new EmptyStackException();
		}
		else {
			return this.top.data;
		}
	}
}

class StackNode {
	char data;
	StackNode next;
	public StackNode(char data) {
		this.data = data;
		this.next = null;
	}
}
