//package test;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

class MagicSquares {

 public static void main(String[] args) {
  try {
   File file = new File("Mercury.txt");
   FileReader fileReader = new FileReader(file);
   BufferedReader bufferedReader = new BufferedReader(fileReader);
   StringBuffer stringBuffer = new StringBuffer();
   String line;
   while ((line = bufferedReader.readLine()) != null) {
    stringBuffer.append(line);
    stringBuffer.append("\n");
   }
   fileReader.close();
   String mercury_square = stringBuffer.toString();
   System.out.println(mercury_square);
   String[] mercury_list = mercury_square.split("\n");
   int length_mercury_list = mercury_list.length;
   String[] mercury_list_list = new String[length_mercury_list];
   for (int i = 0; i <  length_mercury_list; i++) {
       //System.out.println(mercury_list[i]);
       if (mercury_list[i] instanceof String) {
           System.out.println("mercury_list[i] is a string homie");
       }
   }
   for (int i = 0; i < length_mercury_list; i++) {
       String item = mercury_list[i];
       mercury_list[i] = item.split("\t");
   }
   
  } catch (IOException e) {
   e.printStackTrace();
  }
 }
}