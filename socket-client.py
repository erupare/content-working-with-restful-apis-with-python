import socket

HOST = "127.0.0.1"
PORT = 57392

# create a socket for ipv4 and tcp named sock
    
    # connect the socket

    # get the user's name input
    
    # complete to get content_length; length of name

    # formatted header, do not change
    header = """POST / HTTP/1.1 
Host: %s
Content-Type: text/html
Content-Length: %s

""" % (HOST, content_length)

    # create the header and convert to bytes 

    # add body and convert to bytes
    
    # send payload to echo-server

    # receive response, label as "response"

    #  For Office Use Only, Please Do Not Change Code Below
    expected = b"Hello Cloud Guru " + bytes(name, 'utf-b') + b". I am very glad you are here."

    try:
        assert response == expected
    except AssertionError:
        print("Expected: ", expected)
        print("Response: ", response)
        print("They do not match.")
    else:
        print("Congratulations!  You have completed the lab.")





