def process_recording(video_path, out_json):
    import json
    timeline = [{'t':0.0,'emotion':'neutral','bbox':[0,0,10,10]}]
    with open(out_json,'w') as f:
        json.dump(timeline,f)
    return out_json
