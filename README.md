# Compare-config-scraper-output-with-config-API
This repository is my submission for the task #T332647. In this task, we were supposed to compare the API result with scraper output.
<h2>Description</h2>
In this task we were supposed to compare the output from the scrapper we developed as our contribution to the <a href = "https://phabricator.wikimedia.org/T331201">Task #T331201</a> to the results from API. To achieve the same I first parsed the data from the API end-point into a CSV file named "output.csv" using the "parser.py". Then I used "comparison.py" to compare the "output.csv" to the different results from the contribution to task T331201.
<h2>Installation</h2>
To use this program to compare your own generated file to the API result you may follow the following steps:<br>
1. First clone the repository using git clone command.<br>
2. Then add the file that you want to compare in the "Test_files" directory.<br>
3. Make sure that the Format of the file that you want to comapare is like this:<br>
source language, target language, translation engine, other Columns if any<br>
4. Make sure that the first three columns of the header row are same as mentioned above.<br>
5. In the file "comparison.py", change the address in line 4 to the adress of the file you want to compare. <br>
6. Execute the file "comparison.py". You will get the accuracy result on your terminal.
