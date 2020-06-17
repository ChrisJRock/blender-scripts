import bpy
import logging

log = logging.getLogger(__name__)
log.info("Running shape key script experiment...")

def run():
    active_object = bpy.context.active_object
    if active_object is None:
        log.info("No object currently active.")
        return

    shape_key = active_object.active_shape_key
    if shape_key is None:
        log.info("No shape key currently active.")
        return
    
    if shape_key.relative_key is None:
        log.info("Active shape key is not relative to another shape key. This script does not apply.")
        return
    
    normalize_shape_key(active_object , shape_key , True)
    normalize_shape_key(active_object , shape_key , False)
    
def normalize_shape_key (object , shape_key , useMin):
    normalized_shape_key_name = shape_key.name + "_normalized"
    if useMin:
        factor = shape_key.slider_min
        
        if factor == 0:
            log.info("Shape key slider min is '0'. Normalization not necessary for that factor.")
            return
        
        normalized_shape_key_name += "_min"
        
    else:
        factor = shape_key.slider_max
        
        if factor == 1:
            log.info("Shape key slider max is '1'. Normalization not necessary for that factor.")
            return
        
        normalized_shape_key_name += "_max"
    
    normalized_shape_key = object.shape_key_add(name=normalized_shape_key_name , from_mix=False)
    normalized_shape_key.mute = shape_key.mute
    normalized_shape_key.relative_key = shape_key.relative_key
    normalized_shape_key.vertex_group = shape_key.vertex_group
    
    iterable = zip(shape_key.relative_key.data , shape_key.data , normalized_shape_key.data)
    for base , unnormalized , normalized in iterable:
        normalized.co = (unnormalized.co - base.co) * factor + base.co
    
        
run()