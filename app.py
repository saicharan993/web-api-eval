
from web_api_eval import env_config,app

if __name__ == "__main__":
    print(env_config)
    app.run(host= env_config.HOST,
            port= env_config.PORT,
            debug= env_config.DEBUG)