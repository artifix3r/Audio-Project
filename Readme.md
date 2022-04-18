# Content of Project
The goal of the project is to comment on audio file. Once the code is execuded, the small GUI with several buttons will be opened. When 'Load' button is pressed, the file manager is opened and from here user can choose any audio file.
'Play' button is used to play the choosen audio. The others, 'Pause' and 'Stop' are for pausing and stopping the audio, accordingly. The difference is that when the audio is stopped all the comments will be uploaded to JSON file and saved for the upcoming tries to play the audio. In simple words, these comments will be visible for the other users in this case.

There is input area under these buttons which is initially disabled. However, when the user wants to comment, he/she can make this input area 'able' by just simply clicking on 'Add comment' button. After he/she finished commenting, by clicking on 'Save comment' button, the comments can be saved. Finally, the comments will be uploaded to JSON file when the audio completely stopped (by 'Stop' button). Moreover, the user get a notification whether the comment is saved or not. In case if saved, 'comment successfully saved' massege will apper on the GUI. 

Finally, at the bottom of the GUI, the comments and the corresponding time as milliseconds will be visible for the users.

# How to Execute the code
Before execution, the user should install the required libraries which have been used in the code. The most important ones are pygame and tkinter. All these can be installed with just one line of code, !pip install 'library'.\

## You don't have time for installing libraries or you don't want to install libraries ?
    No problem just go into dist file and then double click audiopy file 
    


