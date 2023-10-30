import configparser
import os

def copy_env_to_config():
    try:
        # Print debugging information
        print("Current working directory:", os.getcwd())
        print("DATABASE_URL from environment:", os.environ.get('DATABASE_URL'))
        print("PORT from environment:", os.environ.get('PORT'))

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

            # Read and print the contents immediately
            with open('config.txt', 'r') as f:
                contents = f.read()
            print("Contents of config.txt after writing:")
            print(contents)
        else:
            print("No changes detected for config.txt")

    except Exception as e:
        print("Error updating config.txt:", e)

