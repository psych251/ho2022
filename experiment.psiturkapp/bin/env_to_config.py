import configparser
import os

def copy_env_to_config():
    try:
        c = configparser.ConfigParser()
        c.read('config.txt')

        changed = False
        if 'DATABASE_URL' in os.environ:
            c['Database Parameters']['database_url'] = os.environ['DATABASE_URL']
            changed = True
        if 'PORT' in os.environ:
            c['Server Parameters']['port'] = os.environ['PORT']
            changed = True

        if changed:
            # Print a debugging message before writing
            print("Writing changes to config.txt")
            with open('config.txt', 'w') as out:
                c.write(out)
            print("Changes written to config.txt successfully!")

        else:
            print("No changes detected for config.txt")

    except Exception as e:
        print("Error updating config.txt:", e)

