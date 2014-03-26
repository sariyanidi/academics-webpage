from os.path import splitext, basename
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as stg

import Image as PImage
import os
import hashlib

def content_file_name(instance, filename):
    bname, ext = splitext(basename(filename));

    return str(str(instance.id)+hashlib.sha224(bname).hexdigest()+ext)

def content_file_name_same(instance, filename):
    bname, ext = splitext(basename(filename));

    return str(bname+str(instance.id)+ext)


class GImage(models.Model):
    fname = models.ImageField(upload_to=content_file_name, verbose_name = _('fname'))
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=200,blank=True)
    
    def __str__(self):
        return "default.png" if len(self.fname.name) == 0 else self.fname.name 
    
    def image_tag(self):
        return u'<img src="%s" height=60 />' % os.path.join(stg.MEDIA_URL,self.__str__())
    
    
    image_tag.short_description = 'Headshot'
    image_tag.allow_tags = True
    
    class Meta:
        app_label="blog"
    
    # Save thumbnail
    def saveThumb(self, imType):
        if imType == "l_tn":
            nWidth, nHeight = (stg.L_TN_SIZE,stg.L_TN_SIZE)
        elif imType == "m_tn":
            nWidth, nHeight = (stg.M_TN_SIZE,stg.M_TN_SIZE)
        elif imType == "med":
            nWidth, nHeight = (stg.M_IM_SIZE,stg.M_IM_SIZE)
        
        im = PImage.open(os.path.join(stg.MEDIA_ROOT, self.fname.name))
        im.thumbnail((nWidth, nHeight), PImage.ANTIALIAS)
        
        fn, ext = os.path.splitext(self.fname.name)
        thumbFn = imType + fn + ext

        # make a rectangular image if target is thumbnail
        if imType == "l_tn" or imType == "m_tn":
            thumb = PImage.new('RGBA', (nWidth, nHeight), (255, 255, 255, 0))
            thumb.paste(im, ((nWidth - im.size[0]) / 2, (nHeight - im.size[1]) / 2))
            thumb.save(os.path.join(stg.MEDIA_ROOT, thumbFn))
        # or only resize it otherwise (without putting to center)
        else:
            im.save(os.path.join(stg.MEDIA_ROOT, thumbFn))
            
        
    
    def save(self, *args, **kwargs):
        
        new_item = False
        if self.id == None:
            new_item = True
            
        super(GImage, self).save(*args, **kwargs)
                        
        if new_item:
            # Update the name, let it start with the id of the row
            old_fn = self.fname.name
            self.fname.name = content_file_name(self, self.fname.name)
            os.rename(os.path.join(stg.MEDIA_ROOT, old_fn,), os.path.join(stg.MEDIA_ROOT, self.fname.name))
            super(GImage, self).save(*args, **kwargs)
        
        
        GImage.saveThumb(self,"l_tn")        
        GImage.saveThumb(self,"m_tn")
        GImage.saveThumb(self,"med")
    
    