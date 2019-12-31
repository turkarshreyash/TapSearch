# TapSearch
Using TapSearch is extremely easy!
Tap Search has mainly 3 features:
* Search
* Add
* Clear

### Search
#### For searching a word in paragraphs and pdfs
This functionality is performed by the card number 1 of the home page.

You have to type the word in the text field and click 'Search'

Results will be as following 
##### Paragraphs 


Count of paragraphs in which the search word has occured (always less than 10)
###### Paragraphs Count : 4 

Total number of times word has occured in all paragraphs together.
###### Total Count of word (Para): 5 

Then paragraphs are displayed in descending order of occurance of word.
After paragraphs pdfs are displayed

##### PDFs

Count of PDFs in which the search word has occured
###### PDF Count : 4 

Total number of times word has occured in all pdfs together.
###### Total Count of word (PDF): 5 

Then pdfs are displayed in descending order of ocurance of word.

You can download the pdfs as well.

### Added Para od PDFs
Second card on home page performs this functions
You can upload a pdf or enter paragraphs in text field.

### Clear 
Third card on this page performs this funstions.
All token are cleared and words are deleted.





## How this TapSearch funcions?
Well in this system : 
* first the the entered text or pdf is split into paragraphs. Further this paragraphs are store in 'Paragraphs' & 'PDFStorage' table.
* preprocessing is done in which all words are converted to lower and punctuation marks are removed
* Then words are store in a 'Words' table if they didn't exist and are linked using a RDBMS to paras or pdfs they occured in. 'word_to_para' & 'word_to_pdf' tables are used for the same.

### So when we perform search operation first 'Words' table is checked if the word exists then pdfs and paras in which they occured are retrived using 'word_to_para' & 'word_to_pdf' tables and result is displayed.


 
### Link to Cloud Deployment : https://tapchiefinternassign.herokuapp.com/

