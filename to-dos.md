

### The basic idea behind the bot:

The person will send his code
Then will reply to his own message using a command say `$run`

The bot will then save the message as a `code.py` file

Then the bot will execute the file, while printing the stdout to discord.

- Later stages of bot will include logging into a database for all the code compilation calls
----
## How to 
Steps to build the bot :

>- Setup a basic layout for the Discord Bot

>- Learn how online compilers work to get and idea about how the errors are handled and the cosole output is printed.

>- Setup the bot so that it can save the `quoted` text to a file named `code.py`

>- Found that I should do something like _[ThreadPoolExecutor](https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/), [ThreadPoolExecutor](https://tutorialedge.net/python/concurrency/python-processpoolexecutor-tutorial/)_

>- Helpful Articles:
-[Reading a replied Message](https://stackoverflow.com/questions/67100856/how-can-i-read-the-message-that-someone-replied-to-in-discord-py)