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



## Testing the app

### TestCase 1: Adding 15 paras at once
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque et lectus magna. Donec ac consectetur sapien. Phasellus cursus laoreet scelerisque. Nullam porta fermentum nisi nec tincidunt. Integer tincidunt commodo urna, eu dapibus ex sodales sed. Pellentesque enim lectus, malesuada in ligula ac, tempus dignissim nibh. Cras vitae auctor tortor. Praesent ut semper lorem. Nulla facilisi. Pellentesque rhoncus tortor at mi interdum, at ultrices eros tristique. Duis mollis ac elit eget venenatis. Morbi dictum, urna ac malesuada blandit, nunc metus feugiat leo, eu porta risus nulla ut lacus. Etiam mattis et odio non sodales. Nulla sit amet nunc vitae diam placerat consequat non vel ipsum.

Cras aliquam non justo vel consectetur. Sed dictum leo lacus, non venenatis justo luctus molestie. Morbi at odio eros. Aenean sit amet lacus sit amet elit mollis pellentesque eget sed justo. Suspendisse auctor, arcu quis tincidunt tristique, mi quam venenatis nisi, ac dapibus mauris ipsum quis diam. Vestibulum dolor justo, commodo ut purus vel, ultricies viverra lacus. Praesent porttitor blandit maximus.

Ut posuere consequat quam, ac consectetur urna ultrices sit amet. In viverra enim id ex facilisis, at vestibulum dui vestibulum. Pellentesque ultrices molestie mi, in convallis lectus iaculis id. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Cras augue tellus, lacinia sit amet augue nec, interdum suscipit nisi. Etiam mattis lectus sit amet feugiat bibendum. Morbi mollis nisi quis imperdiet semper.

Mauris malesuada id mauris ut vehicula. Maecenas gravida dictum vulputate. Donec at congue ligula. Aenean sit amet elit vitae sem pellentesque commodo in in felis. Ut viverra ex vel molestie tincidunt. Cras vitae mollis purus. Mauris a lectus ante. Donec viverra consequat nulla, sed blandit orci eleifend sed. Morbi sed molestie mi.

Nullam vel diam eget nibh ultricies pretium. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Praesent sed molestie turpis, non aliquam nisi. Donec ullamcorper vehicula massa, volutpat porttitor eros interdum quis. Nullam feugiat nisl non tellus condimentum, vel blandit metus lobortis. Curabitur condimentum sodales tempus. Maecenas lobortis justo ac elementum ultricies. Donec ultricies tristique elit, sagittis tempus odio efficitur sit amet. Nullam sagittis suscipit eros, fringilla blandit ex tincidunt ut.

Maecenas luctus nibh sed augue sollicitudin, ac hendrerit enim pulvinar. Nunc vel efficitur justo. Curabitur sit amet nisl aliquam, placerat urna eu, accumsan nisl. Etiam eget sodales eros, eget cursus ante. Donec dictum, tortor sit amet semper fringilla, diam nisi pretium dolor, pharetra semper massa diam iaculis sapien. Fusce rhoncus nibh eget gravida dignissim. In hac habitasse platea dictumst. Aliquam facilisis diam mauris, et volutpat odio suscipit non. Fusce tristique lacus quis ipsum convallis, fringilla blandit sem ornare. Phasellus rhoncus purus vel tempus finibus. Cras magna orci, consequat eu nibh at, dictum ultrices risus. Nam volutpat tincidunt efficitur. Nam vel lacus sodales, ultricies ipsum in, vestibulum nisl.

Etiam eleifend nulla efficitur, commodo sapien quis, laoreet dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus et orci vel neque commodo hendrerit. Curabitur egestas quis erat ut viverra. Ut ultrices vel velit eu interdum. Aliquam consequat ut eros dapibus placerat. Nulla ut neque sit amet est scelerisque gravida. Nulla consectetur tempor tellus, et mollis odio ultricies quis. Fusce at dictum nisi. Suspendisse potenti. Quisque posuere enim blandit augue congue, a fringilla lectus porttitor. Pellentesque finibus, elit vitae fringilla faucibus, ligula nulla eleifend neque, vel placerat risus nunc ac odio. Sed ipsum velit, tincidunt eu consequat ac, convallis nec velit. Quisque tortor tortor, semper vitae massa et, euismod molestie arcu.

Aenean egestas nisl purus, a porta lectus bibendum ut. Sed vel mauris sodales, convallis nulla quis, tempor quam. Duis mollis, neque eget suscipit vehicula, lectus ipsum lobortis justo, eu venenatis urna sem eu diam. Ut maximus pulvinar nunc eu posuere. Pellentesque faucibus massa in porta iaculis. Phasellus lacinia urna quis magna pulvinar malesuada. Proin ultricies mattis turpis vitae convallis. Morbi eu turpis bibendum nulla blandit volutpat. Vestibulum faucibus nunc quam, sit amet fringilla ante congue ut. Cras nisi tellus, rutrum sit amet diam ut, ultricies dignissim arcu. Vestibulum id neque porttitor, ornare erat at, hendrerit dui. Phasellus ut ipsum rutrum, tincidunt enim sed, cursus sem. Donec porttitor, nulla eu interdum iaculis, massa lectus consectetur urna, at ultrices dolor nibh eget metus. Cras in eros iaculis, ultricies magna eget, vehicula dolor. Duis volutpat tellus ut tortor cursus ornare.

Sed mattis nibh nec libero sodales, eu suscipit lacus bibendum. Aenean ut sem egestas, pellentesque mi sed, facilisis quam. Nulla non nisi sit amet mauris tristique scelerisque sed eget lorem. Donec at porttitor nulla. Integer consequat eros ut justo finibus vulputate. Aliquam id scelerisque sapien. Morbi lobortis leo in varius eleifend. Phasellus ante ex, consectetur a ultrices vel, posuere vel enim. Etiam nec ullamcorper nunc. Sed tristique massa id dapibus dignissim. Aliquam erat volutpat. Duis maximus justo sit amet nisl sagittis, et finibus turpis vehicula. Morbi ex augue, suscipit congue porta sed, ultricies id neque. Suspendisse ultricies cursus eros et dictum. Donec aliquet, arcu in aliquet rhoncus, elit ipsum bibendum justo, ac pharetra turpis massa sit amet felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;

Quisque iaculis magna at eleifend posuere. Mauris sed nibh tempor, sagittis nibh non, gravida nisl. Praesent tincidunt sagittis est, non imperdiet nisi faucibus ac. Mauris felis nisi, tincidunt a viverra sed, pulvinar a dui. In porttitor, orci eu ultrices varius, leo felis laoreet tellus, vel mattis enim nulla non magna. Vivamus eu arcu metus. Proin id imperdiet libero, vel volutpat enim. Aenean condimentum porttitor ullamcorper. Praesent eleifend commodo velit, convallis finibus neque tempor a. Morbi vel felis mauris. Fusce convallis malesuada ante.

Mauris hendrerit malesuada mi, in ultrices massa placerat non. Fusce ultricies interdum mi nec maximus. Vestibulum varius orci at posuere dapibus. Maecenas et viverra urna. Suspendisse ornare nunc quis risus fermentum egestas. Integer eget est ac libero sodales vestibulum et eu felis. Sed neque eros, facilisis vitae sagittis sit amet, ultrices nec ante. Ut viverra orci pretium viverra sodales. Donec purus quam, ultricies at libero a, ullamcorper sagittis enim.

Donec lorem turpis, condimentum quis risus id, gravida aliquet libero. Phasellus ultricies urna ac imperdiet ultricies. Suspendisse et quam felis. Mauris sed orci feugiat magna varius accumsan. Nulla facilisi. Nullam a ligula ultrices, finibus nibh elementum, egestas neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas viverra, nibh accumsan consequat facilisis, urna justo cursus felis, vitae commodo libero ante vel eros. Nunc id purus rhoncus, egestas quam a, imperdiet enim. Nunc sagittis ligula at luctus pellentesque.

Suspendisse at leo a enim convallis mollis. Maecenas aliquam est urna, id vehicula orci interdum non. Curabitur ex arcu, molestie a ipsum ac, maximus maximus urna. Sed nunc turpis, finibus sit amet est eu, dignissim aliquam ipsum. Integer rutrum lectus eu consequat efficitur. Nunc malesuada malesuada elit eget ultrices. Maecenas sit amet est tortor. Nunc imperdiet faucibus lorem, id tincidunt diam tincidunt sed. Mauris venenatis massa sit amet augue facilisis, non ultricies justo bibendum.

Nulla sodales ex quis enim pharetra molestie. Morbi felis nisl, auctor vulputate dolor a, convallis sollicitudin augue. Donec vehicula semper porttitor. Nunc semper consequat justo, at placerat tellus maximus nec. Quisque finibus ornare dolor, eget rhoncus nulla dictum ac. Ut pharetra magna quis sem tincidunt, et porta dolor hendrerit. Vivamus eget sodales massa. Donec molestie magna vel enim fringilla, tincidunt dapibus nisl aliquam. Duis nec aliquam sem. Suspendisse posuere auctor mi, pharetra auctor magna lobortis porta. In vel eleifend dolor. Donec lacinia posuere odio quis iaculis. Nullam lacinia libero quis vulputate egestas.

Pellentesque purus nunc, varius quis dolor vel, viverra tristique purus. Praesent id justo quam. Vivamus scelerisque consectetur auctor. Suspendisse dapibus maximus mi, sit amet varius risus ullamcorper ac. Phasellus rhoncus, orci elementum malesuada gravida, ligula eros tincidunt velit, auctor vestibulum ipsum elit a lacus. Duis cursus blandit nisl. Ut sollicitudin diam non pretium volutpat. Proin sapien metus, tempor id sodales sit amet, dapibus in augue. Nullam nisl velit, dignissim sed orci non, eleifend tincidunt odio. Vivamus in aliquet libero.
### Result : Pass

### TestCase 2 : Search for lorem
Paragraphs Count : 4

Total Count of word (Para): 5
Word Occurance : 2

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque et lectus magna. Donec ac consectetur sapien. Phasellus cursus laoreet scelerisque. Nullam porta fermentum nisi nec tincidunt. Integer tincidunt commodo urna, eu dapibus ex sodales sed. Pellentesque enim lectus, malesuada in ligula ac, tempus dignissim nibh. Cras vitae auctor tortor. Praesent ut semper lorem. Nulla facilisi. Pellentesque rhoncus tortor at mi interdum, at ultrices eros tristique. Duis mollis ac elit eget venenatis. Morbi dictum, urna ac malesuada blandit, nunc metus feugiat leo, eu porta risus nulla ut lacus. Etiam mattis et odio non sodales. Nulla sit amet nunc vitae diam placerat consequat non vel ipsum.


Word Occurance : 1

    Sed mattis nibh nec libero sodales, eu suscipit lacus bibendum. Aenean ut sem egestas, pellentesque mi sed, facilisis quam. Nulla non nisi sit amet mauris tristique scelerisque sed eget lorem. Donec at porttitor nulla. Integer consequat eros ut justo finibus vulputate. Aliquam id scelerisque sapien. Morbi lobortis leo in varius eleifend. Phasellus ante ex, consectetur a ultrices vel, posuere vel enim. Etiam nec ullamcorper nunc. Sed tristique massa id dapibus dignissim. Aliquam erat volutpat. Duis maximus justo sit amet nisl sagittis, et finibus turpis vehicula. Morbi ex augue, suscipit congue porta sed, ultricies id neque. Suspendisse ultricies cursus eros et dictum. Donec aliquet, arcu in aliquet rhoncus, elit ipsum bibendum justo, ac pharetra turpis massa sit amet felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;


Word Occurance : 1

    Donec lorem turpis, condimentum quis risus id, gravida aliquet libero. Phasellus ultricies urna ac imperdiet ultricies. Suspendisse et quam felis. Mauris sed orci feugiat magna varius accumsan. Nulla facilisi. Nullam a ligula ultrices, finibus nibh elementum, egestas neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas viverra, nibh accumsan consequat facilisis, urna justo cursus felis, vitae commodo libero ante vel eros. Nunc id purus rhoncus, egestas quam a, imperdiet enim. Nunc sagittis ligula at luctus pellentesque.


Word Occurance : 1

    Suspendisse at leo a enim convallis mollis. Maecenas aliquam est urna, id vehicula orci interdum non. Curabitur ex arcu, molestie a ipsum ac, maximus maximus urna. Sed nunc turpis, finibus sit amet est eu, dignissim aliquam ipsum. Integer rutrum lectus eu consequat efficitur. Nunc malesuada malesuada elit eget ultrices. Maecenas sit amet est tortor. Nunc imperdiet faucibus lorem, id tincidunt diam tincidunt sed. Mauris venenatis massa sit amet augue facilisis, non ultricies justo bibendum.


PDFs

No Results in PDF!
### Result : Pass

### TestCase 3 : Add PDF
Lorem-Ipsum.pdf
### Result : Pass

### TestCase 4 : Search for 

Paragraphs Count : 10

Total Count of word (Para): 15
Word Occurance : 2

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque et lectus magna. Donec ac consectetur sapien. Phasellus cursus laoreet scelerisque. Nullam porta fermentum nisi nec tincidunt. Integer tincidunt commodo urna, eu dapibus ex sodales sed. Pellentesque enim lectus, malesuada in ligula ac, tempus dignissim nibh. Cras vitae auctor tortor. Praesent ut semper lorem. Nulla facilisi. Pellentesque rhoncus tortor at mi interdum, at ultrices eros tristique. Duis mollis ac elit eget venenatis. Morbi dictum, urna ac malesuada blandit, nunc metus feugiat leo, eu porta risus nulla ut lacus. Etiam mattis et odio non sodales. Nulla sit amet nunc vitae diam placerat consequat non vel ipsum.


Word Occurance : 2

    Maecenas luctus nibh sed augue sollicitudin, ac hendrerit enim pulvinar. Nunc vel efficitur justo. Curabitur sit amet nisl aliquam, placerat urna eu, accumsan nisl. Etiam eget sodales eros, eget cursus ante. Donec dictum, tortor sit amet semper fringilla, diam nisi pretium dolor, pharetra semper massa diam iaculis sapien. Fusce rhoncus nibh eget gravida dignissim. In hac habitasse platea dictumst. Aliquam facilisis diam mauris, et volutpat odio suscipit non. Fusce tristique lacus quis ipsum convallis, fringilla blandit sem ornare. Phasellus rhoncus purus vel tempus finibus. Cras magna orci, consequat eu nibh at, dictum ultrices risus. Nam volutpat tincidunt efficitur. Nam vel lacus sodales, ultricies ipsum in, vestibulum nisl.


Word Occurance : 2

    Aenean egestas nisl purus, a porta lectus bibendum ut. Sed vel mauris sodales, convallis nulla quis, tempor quam. Duis mollis, neque eget suscipit vehicula, lectus ipsum lobortis justo, eu venenatis urna sem eu diam. Ut maximus pulvinar nunc eu posuere. Pellentesque faucibus massa in porta iaculis. Phasellus lacinia urna quis magna pulvinar malesuada. Proin ultricies mattis turpis vitae convallis. Morbi eu turpis bibendum nulla blandit volutpat. Vestibulum faucibus nunc quam, sit amet fringilla ante congue ut. Cras nisi tellus, rutrum sit amet diam ut, ultricies dignissim arcu. Vestibulum id neque porttitor, ornare erat at, hendrerit dui. Phasellus ut ipsum rutrum, tincidunt enim sed, cursus sem. Donec porttitor, nulla eu interdum iaculis, massa lectus consectetur urna, at ultrices dolor nibh eget metus. Cras in eros iaculis, ultricies magna eget, vehicula dolor. Duis volutpat tellus ut tortor cursus ornare.


Word Occurance : 2

    Sed mattis nibh nec libero sodales, eu suscipit lacus bibendum. Aenean ut sem egestas, pellentesque mi sed, facilisis quam. Nulla non nisi sit amet mauris tristique scelerisque sed eget lorem. Donec at porttitor nulla. Integer consequat eros ut justo finibus vulputate. Aliquam id scelerisque sapien. Morbi lobortis leo in varius eleifend. Phasellus ante ex, consectetur a ultrices vel, posuere vel enim. Etiam nec ullamcorper nunc. Sed tristique massa id dapibus dignissim. Aliquam erat volutpat. Duis maximus justo sit amet nisl sagittis, et finibus turpis vehicula. Morbi ex augue, suscipit congue porta sed, ultricies id neque. Suspendisse ultricies cursus eros et dictum. Donec aliquet, arcu in aliquet rhoncus, elit ipsum bibendum justo, ac pharetra turpis massa sit amet felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;


Word Occurance : 2

    Suspendisse at leo a enim convallis mollis. Maecenas aliquam est urna, id vehicula orci interdum non. Curabitur ex arcu, molestie a ipsum ac, maximus maximus urna. Sed nunc turpis, finibus sit amet est eu, dignissim aliquam ipsum. Integer rutrum lectus eu consequat efficitur. Nunc malesuada malesuada elit eget ultrices. Maecenas sit amet est tortor. Nunc imperdiet faucibus lorem, id tincidunt diam tincidunt sed. Mauris venenatis massa sit amet augue facilisis, non ultricies justo bibendum.


Word Occurance : 1

    Cras aliquam non justo vel consectetur. Sed dictum leo lacus, non venenatis justo luctus molestie. Morbi at odio eros. Aenean sit amet lacus sit amet elit mollis pellentesque eget sed justo. Suspendisse auctor, arcu quis tincidunt tristique, mi quam venenatis nisi, ac dapibus mauris ipsum quis diam. Vestibulum dolor justo, commodo ut purus vel, ultricies viverra lacus. Praesent porttitor blandit maximus.


Word Occurance : 1

    Ut posuere consequat quam, ac consectetur urna ultrices sit amet. In viverra enim id ex facilisis, at vestibulum dui vestibulum. Pellentesque ultrices molestie mi, in convallis lectus iaculis id. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Cras augue tellus, lacinia sit amet augue nec, interdum suscipit nisi. Etiam mattis lectus sit amet feugiat bibendum. Morbi mollis nisi quis imperdiet semper.


Word Occurance : 1

    Nullam vel diam eget nibh ultricies pretium. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Praesent sed molestie turpis, non aliquam nisi. Donec ullamcorper vehicula massa, volutpat porttitor eros interdum quis. Nullam feugiat nisl non tellus condimentum, vel blandit metus lobortis. Curabitur condimentum sodales tempus. Maecenas lobortis justo ac elementum ultricies. Donec ultricies tristique elit, sagittis tempus odio efficitur sit amet. Nullam sagittis suscipit eros, fringilla blandit ex tincidunt ut.


Word Occurance : 1

    Etiam eleifend nulla efficitur, commodo sapien quis, laoreet dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus et orci vel neque commodo hendrerit. Curabitur egestas quis erat ut viverra. Ut ultrices vel velit eu interdum. Aliquam consequat ut eros dapibus placerat. Nulla ut neque sit amet est scelerisque gravida. Nulla consectetur tempor tellus, et mollis odio ultricies quis. Fusce at dictum nisi. Suspendisse potenti. Quisque posuere enim blandit augue congue, a fringilla lectus porttitor. Pellentesque finibus, elit vitae fringilla faucibus, ligula nulla eleifend neque, vel placerat risus nunc ac odio. Sed ipsum velit, tincidunt eu consequat ac, convallis nec velit. Quisque tortor tortor, semper vitae massa et, euismod molestie arcu.


Word Occurance : 1

    Pellentesque purus nunc, varius quis dolor vel, viverra tristique purus. Praesent id justo quam. Vivamus scelerisque consectetur auctor. Suspendisse dapibus maximus mi, sit amet varius risus ullamcorper ac. Phasellus rhoncus, orci elementum malesuada gravida, ligula eros tincidunt velit, auctor vestibulum ipsum elit a lacus. Duis cursus blandit nisl. Ut sollicitudin diam non pretium volutpat. Proin sapien metus, tempor id sodales sit amet, dapibus in augue. Nullam nisl velit, dignissim sed orci non, eleifend tincidunt odio. Vivamus in aliquet libero.


PDFs

PDF Count : 1

Total Count of word (PDF): 13
Word Occurance : 13

    Download Document


### Result : Pass


### TestCase 5 : Clear
### Result : Pass

### TestCase 6 : Search for lorem

Paragraphs
No Results in paras!
PDFs

No Results in PDF!

### Result : Pass