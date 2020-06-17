import bpy
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)-15s %(levelname)8s %(name)s %(message)s')

for name in ('blender_id', 'blender_cloud'):
    logging.getLogger(name).setLevel(logging.DEBUG)

def register():
    pass

log = logging.getLogger(__name__)
log.info("Log config complete.")