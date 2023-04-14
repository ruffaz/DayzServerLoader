import json
import os

def load_mods(mods_json_path):
    mods = {}
    if os.path.exists(mods_json_path):
        with open(mods_json_path, "r") as f:
            mods = json.load(f)
            print(f"Loaded mods: {mods}")
    return mods

def save_mods(mods_json_path, mods):
    with open(mods_json_path, "w") as f:
        json.dump(mods, f)

def load_paths(paths_json_path):
    server_path, workshop_path = "", ""
    if os.path.exists(paths_json_path):
        with open(paths_json_path, "r") as f:
            paths_data = json.load(f)
            server_path = paths_data.get("server_path", "")
            workshop_path = paths_data.get("workshop_path", "")
    return server_path, workshop_path

def save_paths(paths_json_path, paths):
    with open(paths_json_path, "w") as f:
         f.write(json.dumps(paths))


def store_dz_config(mods_json_path, mod_list_name, dzconfig_path):
    if os.path.exists(mods_json_path):
        with open(mods_json_path, "r") as f:
            data = json.load(f)

        data["mod_lists"][mod_list_name]["dz_config"] = dzconfig_path

        with open(mods_json_path, "w") as f:
            json.dump(data, f, indent=4)

def load_configs(configs_json_path):
    configs = {}
    if os.path.exists(configs_json_path):
        with open(configs_json_path) as f:
            data = json.load(f)
            print("Loaded configs data:", data)
            mod_lists = data.get("mod_lists", {})
            for mod_list_name, mod_list_data in mod_lists.items():
                configs[mod_list_name] = {"configs": mod_list_data.get("configs", {})}
    return configs
