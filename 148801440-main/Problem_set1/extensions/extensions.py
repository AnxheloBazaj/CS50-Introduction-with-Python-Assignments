def main():
    file_name = input('File name:').lower() # Prompt the user for the name of a file and convert to lowercase

    if '.gif' in file_name:     # Check if the file’s name ends in any of these suffixes and then output
        print('image/gif')      # the files media type
    elif '.jpg' in file_name or '.jpeg' in file_name:
        print('image/jpeg')
    elif '.png' in file_name:
        print('image/png')
    elif '.pdf' in file_name:
        print('application/pdf')
    elif '.txt' in file_name:
        print('text/plain')
    elif '.zip' in file_name:
        print('application/zip')
    else:
        print('application/octet-stream')

main() # Call main

# Resources used :  developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

