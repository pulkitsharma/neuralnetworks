#!/usr/bin/env python2.7
import gtk.gdk

def saveImage():
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    #pb = pb.get_from_drawable(w,w.get_colormap(),510,340,50,50,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),510,340,0,0,50,50)
    if (pb != None):
        pb.save("screenshot.png","png")
        print "Screenshot saved to screenshot.png."
    else:
        print "Unable to get the screenshot."

#saveImage()
 
