# Critical Code Snippets

> ### 1. Check user input...
>
> <img src="Images\1. check user input.png" style="margin:0; width:450px; height:200px; background-color:red">
>
> 
>
> ### 2. Read/Write in the files...
>
> <img src="Images\2. file handling.png" style="margin:0; width:450px; height:200px; background-color:red">
>
> 
>
> ### 3. Coloring Terminal Texts...
>
> **=> init(autoreset=true) :**
>
> - Resets the terminal color to the default one after applicating each coloring process, (writing this line at begginning of the function make you don't have to manually reset it after each print statement).
>
> **=> Back.specific_color :**
>
> - Detect the back-color of the text.
>
> **=> Fore.specific_color :**
>
> - Detect the text color itself.
>
> <img src="Images\\3. Coloring Terminal Text.png" style="margin:0; width:400px; height:100px; background-color:red">
>
> ### 4. The Path Handling Functions...
>
> **=> strip("") :**
>
> - removes what you write inside the double quotes a string.
>
> **=> isdir(a_file_path) :**
>
> - check if [a_file_path] is (a directory path) in your PC or not, (Boolean Function).
>
> **=> listdir(a_path) :**
>
> - the output is a (List Datatype) of all entries(files or sub-directories) inside (the directory path) you gave to [listdir function].
>
> **splitext(a_file_path) :**
>
> - the output is a (Tuple Datatype), it splits a file path into (a file root or file path without the extension) & (a file extension including the dot).
>
> **=> join("a_string", "a_string") :**
>
> -  joins one or more path components into a single path, and automatically adding any necessary directory separators (`/` or `\`) between them.
>
> **=> isfile(a_path) :**
>
> - (Boolean Output) represents if (the path) you gave to this function matches existing file in (this path) or not.
>
> 
>
> ### 5. Ternary Conditional Statement...
>
> - It allows you to evaluate an expression and return one of two values based on a condition, (Note: all in a single line).
>
> ​	<img src="Images\4. Ternary Conditional Statement.png" style="margin:0; width:800px; height:110px; background-color:red">
