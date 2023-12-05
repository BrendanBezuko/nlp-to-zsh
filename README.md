# nlp-to-zsh

![GIF of usage](screenshots/this.gif)

## Brief Description
`nlp-to-zsh` is a very simple and cutting-edge tool that seamlessly integrates Natural Language Processing (NLP) services, like OpenAI, with the Zsh command line. It allows users to type commands in plain English and receive command line suggestions, enhancing the user experience and efficiency.

## Disclaimer
**Use at Your Own Risk**: This tool is provided without any guarantees or warranty. It sends data from the command line buffer to OpenAI or other NLP services. Note that the commands generated may not always work as expected and could potentially cause harm to your system resulting in data loss. Please proceed with caution and at your own risk. Intended as a tool to learn how to use the linux command line faster than ever before.

## What it Does and How to Use
Simply type what you want to do in plain English and press `Ctrl+G`. Choose from the listed options, and the command will magically appear in your command line buffer. 

**Supported Systems**: `nlp-to-zsh` is fine-tuned and tested primarily for GNU/Linux systems. MacOS users might experience certain limitations.

## Setup and Installation
1. **Install Dependencies**: Ensure `zsh`, `python`, and `fzf` are installed on your system.

2. **Python Requirements**: Install the Python dependencies listed in `pip install -r requirements.txt`

3. **Script Installation**: Place `cp ask_gpt.py /usr/local/bin/ && sudo chmod +x /usr/local/bin/ask_gpt.py
cp nlp-to.zsh /usr/local/bin/ && sudo chmod +x /usr/local/bin/nlp-to.zsh`

4. **OpenAI Setup**:
Obtain an API key from OpenAI, and fine tune a model with provided data (I used gpt3-turbo with great results). Take note of model name. 

5. **Shell Integration**:
`cat << EOF > .zshrc
source /usr/local/bin/nlp-tool.zsh
export OPENAI_API_KEY='your_key_here'
export OPENAI_MODEL_NAME='your_model_here'
EOF`

6. **Open new shell**: Open a new instance of zsh or source `. .zshrc`

## Future Plans and Features
- Built in automated testing environment allowing user to quickly sandbox commands.
- Support for multiple APIs for quickly accessing various models.
- Support for locally hosted models (transformers, ollama, etc)
- Enhanced fine-tuning datasets and models.
- Caching mechanism for previous results

## Inspiration
When i first started using linux, learning the linux command-line was often shifting through stackoverflow posts, man pages, and blog posts. I remember dreaming I could just use natural language to quickly reference commands or write a simple scripts. Modren technology makes this possible. I hope this tool acts a beast for you to learn the command line quickly and effectivly. Enjoy.

## Credits
Developed by myself with modren programming tools. All contributions are deeply appreciated.

Enjoy using `nlp-to-zsh`!
