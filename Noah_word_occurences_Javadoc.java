
// Alysha Noah
// 7/19/2020
// Noah_word_occurences
// count the most frequent word occurrences from play.txt and use Javadoc

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class Noah_word_occurences_Javadoc {

	// main method
	public static void main(String[] args) throws Exception {
		
		// create line variable
		String line = "";
		ArrayList<String> words = new ArrayList<String>(); // create words array to store string

		// create file and buffRead variable to open play.txt and read
		FileReader file = new FileReader("play.txt");
		BufferedReader buffRead = new BufferedReader(file);

		// read each line from play
		while ((line = buffRead.readLine()) != null) {
			// split text and change to lower case
			String string[] = line.toLowerCase().split("([`~@#%^&*:!-_',.\\s]+)");
			
			// place all split and lower case words into words array
			for (String s : string) {
				words.add(s);
			}
		}
		
		// create map to go through list and sort and count
		Map<String, Integer> map = new HashMap<>();
		for (String w : words) {
			Integer n = map.get(w);
			n = (n == null) ? 1 : ++n;
			map.entrySet().stream().limit(10);
			map.put(w, n);
			
			// limit results to only top 10 most frequent
			List<Entry<String, Integer>> result = map.entrySet().stream()
					.sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())).limit(10)
					.collect(Collectors.toList());
			
			
				for (Entry<String, Integer> l : result) {
				
					System.out.println(l);

				
			}

			// display in vertical order
			/*for (Entry<String, Integer> l : result) {

				// print each line from result
				System.out.println(l);

			}*/

		}
		// close the buffered reader
		buffRead.close();
	} // end main

}// end class
