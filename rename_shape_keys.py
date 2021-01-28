import bpy
import logging
print
log = logging.getLogger(__name__)
log.info("Renaming shape keys ...")

def rename_shape_keys(test_mode):
    active_object = bpy.context.active_object
    if active_object is None:
        log.info("ERROR: No object currently active.")
        return
    
    filepath = bpy.path.abspath("//rename-map.txt")
    log.info("Rename map filepath: '" + filepath + "'.")
    shape_keys = active_object.data.shape_keys.key_blocks
    file = open (filepath)
    if file is None:
        log.info("Rename map file not found.")
        return
    
    log.info("Rename map file loaded.")
    with file as text:
        for line in text.readlines():
            line_array = line.split("=>")
            if len(line_array) != 2:
                log.info("ERROR: Unparsable line '" + line + "'.")
                continue
            
            name_a = line_array[0].strip()
            name_b = line_array[1].strip()

            if shape_keys.get(name_a) is None:
                log.info("No shape key found with name '" + name_a + "'.")
                continue
            
            shape_key = shape_keys[name_a]
            
            if shape_keys.get(name_b) is not None:
                log.info("Shape key with name '" + name_b + "' already present.")
                continue
            
            test_log = ""
            if test_mode == False:
                shape_key.name = name_b
            else:
                test_log = "(TEST) "
            
            log.info(test_log + "Renamed shape key '" + name_a + "' to '" + name_b + "'.")

rename_shape_keys(True)