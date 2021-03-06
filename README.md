Sublime Anti Quit
=================

 A very simple plugin, that provides accidental-quitting protection for Sublime Text 2 and 3.

## Usage

The plugin is automatically mapped to the quit keyboard shortcut, to prevent you from accidentally closing Sublime. A prompt will appear, asking if you are sure you want to quit. Press `enter` to quit and `esc` to dismiss it.

The default OS mappings are:

OS X: `Cmd+q` - Windows: `Alt+F4` - Linux: `Ctrl+q`


## Installation

The plugin is not in Package Control yet. Untill it is, the easiest way is to clone this repo into your Packages folder.

Please use the following instructions, depending on your OS. *Note: If you use Sublime Text 2, just replace the `3` with a `2` in the path.*

### On OS X

	$ git clone git@github.com:vanjacosic/sublime-anti-quit.git \
	 ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/AntiQuit
	

### On Windows

	$ git clone git@github.com:vanjacosic/sublime-anti-quit.git "%APPDATA%\SublimeText 3\Packages\AntiQuit"

*Thanks to [Jakob Holmelund](https://github.com/jakobholmelund) for the Windows instructions and testing it out.*

## Notes

This plugin is released under the MIT License.

This is my first Sublime plugin, so please let me know if there is something to improve or do in a better way. Feel free to open an issue or a pull request.
