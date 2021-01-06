'''
HTML Exporter Module.
It generates an HTML table, using Bootstrap as framework.
The generated page needs an Internet connection
in order to load the stylesheet and the scripts.
You can download the .css and .js files to have it working offline.
'''
import time
import socket


class HTMLExporter:

    def __init__(self, playlistName, filename="index.html"):
        ''' Object constructor: opens the given file in
            write mode (destroying the old content) and
            writes HTML code in it.
        '''
        self.tracksCounter = 1  # Counter used in HTMLExporter::addRow()
        self.filename = filename
        try:
            self.outputFile = open(filename, "w")
            self.outputFile.write(self.startHTML(playlistName))
        except OSError:
            print("Error while opening " + filename)
            self.outputFile = None

    def __del__(self):
        ''' Object destructor: writes the HTML table ending,
            the last update date, and closes the file.
        '''
        if self.outputFile is not None:
            # Swap %d and %m if you prefer mm-dd-yyyy
            now = time.strftime("%d/%m/%Y")
            sourceHTML = '<a class="text-light float-right" href='
            sourceHTML += '"https://github.com/0x07cc/spotify-exporter"'
            sourceHTML += ">Source on GitHub</a>"
            name = socket.getfqdn()  # Hostname
            endingHTML = "          </tbody>\n        </table>\n        "
            endingHTML += '<footer class="text-light ml-1">'
            endingHTML += f'Updated on {now} by {name} {sourceHTML}</footer>\n'
            endingHTML += "      </div>\n    </body>\n</html>"
            self.outputFile.write(endingHTML)
            self.outputFile.close()
            print(f"File {self.filename} created.")

    def addRow(self, track):
        ''' Method that generates HTML code for the given track, writes it
            in the output file and updates the counter for the track position.
            Input 'track' is an object (Class Track).
        '''
        if self.outputFile is not None:
            rowHTML = '            <tr>\n              '
            rowHTML += f'<th scope="row">{self.tracksCounter}</th>'
            rowHTML += '\n              '
            rowHTML += f'<td>{track.name}</td><td>{track.artist}</td>'
            rowHTML += f'<td>{track.album}</td>\n            '
            rowHTML += '</tr>\n'
            self.outputFile.write(rowHTML)
            self.tracksCounter = self.tracksCounter + 1

    def startHTML(self, playlistName):
        ''' Method that returns HTML code containing .css and .js files
            needed for Bootstrap.
            'playlistName' is a string, used in the <title> and <h1> tags.
        '''
        return '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Playlist "''' + playlistName + '''"</title>
  </head>
  <body class="bg-dark">
    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    <div class="container-fluid">
      <h1 class="text-light">Playlist "''' + playlistName + '''"</h1>
        <table class="table table-hover table-dark">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">Artist</th>
              <th scope="col">Album</th>
            </tr>
          </thead>
          <tbody>
'''
