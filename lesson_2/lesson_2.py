import asyncio
import logging
import sys

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    asyncio.run(main())