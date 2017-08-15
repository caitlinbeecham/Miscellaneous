import java.util.*;
/*
class Book {
    String title;
    boolean borrowed;
// Creates a new Book
    public Book(String bookTitle) {
        title = bookTitle;
        borrowed = false;
// Implement this method
    }
// Marks the book as rented
    public void borrowed() {
        borrowed = true;
// Implement this method
    }
// Marks the book as not rented
    public void returned() {
        borrowed = false;
// Implement this method
    }
// Returns true if the book is rented, false otherwise
    public boolean isBorrowed() {
        return borrowed;
// Implement this method
    }
// Returns the title of the book
    public String getTitle() {
        return title;
// Implement this method
    } 
}
*/
public class Library {
// Add the missing implementation to this class
    String address;
    ArrayList<Book> bookCollection;
    /* Non Static Methods needed:
     * addBook(string bookTitle) 
     * printAdress()
     * printAvailableBooks()
     * borrowBook()
     * returnBook()
     * 
     * Static Methods Needed:
     * printOpeningHours()
     * printAdress()
     */
    public Library(String libraryAddress) {
        address = libraryAddress;
        bookCollection = new ArrayList<Book>();
    }
    
    public void addBook(Book newBook) {
        //Book newBook = new Book(bookTitle);
        bookCollection.add(newBook);
    }
    
    public void printAddress() {
        System.out.println(address);
    }
    
    public void printAvailableBooks() {
        if (bookCollection.size() == 0) {
            System.out.println("No book in catalog");
        }
        else {
            String bookTitle = "";
            for (int i = 0; i < bookCollection.size(); i++) {
                bookTitle = bookCollection.get(i).getTitle();
                if (bookCollection.get(i).isBorrowed() == false) {
                    System.out.println(bookTitle);
                }
            }
        }
    }
    
    public void borrowBook(String bookTitle) {
        boolean foundCopy = false;
        boolean foundAvailableCopy = false;
        for (int i = 0; i < bookCollection.size(); i++) {
            String title = bookCollection.get(i).getTitle();
            if (title.equals(bookTitle)) {
                foundCopy = true;
            }
            if ((title.equals(bookTitle)) && !(bookCollection.get(i).isBorrowed())) {
                foundAvailableCopy = true;
                bookCollection.get(i).borrowed();
                System.out.println("You successfully borrowed " + bookTitle + ".");
                break;
            }
        }
        if (foundCopy && !(foundAvailableCopy)) {
            System.out.println("Sorry, this book is already borrowed.");
        }
        if (!foundCopy) {
            System.out.println("Sorry, this book is not in our catalog.");
        }
    }
    
    public void returnBook(String bookTitle) {
        for (int i = 0; i < bookCollection.size(); i++) {
            String title = bookCollection.get(i).getTitle();
            if (title.equals(bookTitle)) {
                bookCollection.get(i).returned();
                System.out.println("You successfully returned " + bookTitle + ".");
                break;
            }
        }
        
    }
    
    public static void printOpeningHours() {
        System.out.println("Libraries are open daily from 9am to 5pm.");
    }

    
    public static void main(String[] args) {
        
// Create two libraries
        Library firstLibrary = new Library("10 Main St.");
        Library secondLibrary = new Library("228 Liberty St.");
// Add four books to the first library
        firstLibrary.addBook(new Book("The Da Vinci Code"));
        firstLibrary.addBook(new Book("Le Petit Prince"));
        firstLibrary.addBook(new Book("A Tale of Two Cities"));
        firstLibrary.addBook(new Book("The Lord of the Rings"));
// Print opening hours and the addresses
        System.out.println("Library hours:");
        printOpeningHours();
        System.out.println();
        System.out.println("Library addresses:");
        firstLibrary.printAddress();
        secondLibrary.printAddress();
        System.out.println();
// Try to borrow The Lords of the Rings from both libraries
        System.out.println("Borrowing The Lord of the Rings:");
        firstLibrary.borrowBook("The Lord of the Rings");
        firstLibrary.borrowBook("The Lord of the Rings");
        secondLibrary.borrowBook("The Lord of the Rings");
        System.out.println();
// Print the titles of all available books from both libraries
        System.out.println("Books available in the first library:");
        firstLibrary.printAvailableBooks();
        System.out.println();
        System.out.println("Books available in the second library:");
        secondLibrary.printAvailableBooks();
        System.out.println();
// Return The Lords of the Rings to the first library
        System.out.println("Returning The Lord of the Rings:");
        firstLibrary.returnBook("The Lord of the Rings");
        System.out.println();
// Print the titles of available from the first library
        System.out.println("Books available in the first library:");
        firstLibrary.printAvailableBooks();
    }
    
}