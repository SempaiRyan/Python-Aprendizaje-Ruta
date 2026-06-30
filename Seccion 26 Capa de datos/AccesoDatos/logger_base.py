import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler("capa_datos.log", encoding="utf-8"),
                    log.StreamHandler()
                ]

                )

if __name__ == "__main__":
    log.info("Mensaje nivel Inicial")

    log.debug("Mensaje nivel Debug")

    log.info("Mensaje nivel Info")

    log.warning("Mensaje nivel Warning")

    log.error("Mensaje nivel Error")
