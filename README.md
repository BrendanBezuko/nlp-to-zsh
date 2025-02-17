# nlp-to-zsh

![GIF of usage](screenshots/this.gif)

## Brief Description
Generate commands faster than ever before. Nlp-to-zsh is a cutting-edge tool that seamlessly integrates Natural Language Processing (NLP) services, like OpenAI's ChatGPT, with the Zsh command line. It allows users to type commands in plain English and receive command line suggestions, enhancing the user experience and efficiency.

## Disclaimer:
Use at Your Own Risk. This tool is provided without guarantees or warranty. It sends data from the command line buffer to OpenAI or other NLP services. Note that the commands generated may not always work as expected and could potentially cause harm to your system resulting in data loss. Please proceed with caution and at your own risk. I highly recommend using it in a virtual environment first.

## What it Does and How to Use
Type what you want to do in plain English and press `Ctrl+G`. Choose from the listed options, and the command will magically appear in your command line buffer.

## Supported Systems: 
Nlp-to-zsh is fine-tuned and tested primarily for GNU/Linux systems. MacOS users might experience certain limitations.

## Setup and Installation
 1. **Install Dependencies:** Ensure `zsh`, `python`, and `fzf` are installed on your system.
 2. **Python Requirements:** Install the Python dependencies listed in `pip install -r requirements.txt` (note if you're on Arch Linux you can also `sudo pacman -S python-openai`)
 3. **Script Installation:** `cp ask_gpt.py /usr/local/bin/ && chmod +x /usr/local/bin/ask_gpt.py` and `cp nlp-to.zsh /usr/local/bin/ && chmod +x /usr/local/bin/nlp-to.zsh`. You may need to use elevated permissions with the `sudo` command.
 4. **OpenAI Setup:** Obtain an API key from OpenAI, and fine-tune a model with provided data (I used gpt3-turbo with great results). Take note of the model name.
 5. **Shell Integration:** Append the file `~/.zshrc` with the following lines `source /usr/local/bin/nlp-to.zsh`, `export OPENAI_API_KEY='your_key_here'`, and `export OPENAI_MODEL_NAME='your_model_here'`.
 6. **Open new shell:** Open a new instance of `zsh` or source with this command: `. .zshrc` or `source ~/.zshrc`.

## Future Plans and Features
 - Built-in automated testing environment allowing users to quickly sandbox commands.
 - Support for multiple APIs for quickly accessing various models.
 - Support for locally hosted models.
 - Enhanced fine-tuning datasets and models.
 - Caching mechanism for previous results

## Inspiration
When I first began using Linux, learning the Linux command line was often sifting through Stackoverflow posts, man pages, and blog posts. I remember dreaming I could use natural language to quickly reference commands or write simple scripts. Modern technology makes this possible. I hope this project is a great tool for you to learn the command line quickly and effectively. 

## Credits
Developed by myself. All contributions are deeply appreciated.

**Enjoy using nlp-to-zsh!**
