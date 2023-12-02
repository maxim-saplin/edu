import json
import pandas as pd
from pandas import json_normalize

# Sample JSON data
input = {
    "2019-04-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-04-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-05-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-06-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-07-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-08-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-09-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-10-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-11-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2019-12-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-01-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-02-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-03-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-04-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-05-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-06-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-07-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-08-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-09-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-10-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-11-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2020-12-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-01-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-02-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-03-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-04-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-05-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-06-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-07-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-08-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-09-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-10-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-11-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2021-12-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-01-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-02-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-03-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-04-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-05-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-06-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-07-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-08-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-09-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-10-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-11-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2022-12-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-01-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-02-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-03-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-04-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-05-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-06-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-07-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-02": {
        "comments": {
            "total": 1
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 3,
            "like": 2,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 85,
            "average_read_time_in_seconds": 265,
            "total_read_time_in_seconds": 22525
        }
    },
    "2023-08-03": {
        "comments": {
            "total": 5
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 44,
            "average_read_time_in_seconds": 465,
            "total_read_time_in_seconds": 20460
        }
    },
    "2023-08-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 41,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 615
        }
    },
    "2023-08-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 1,
            "like": 1,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 1,
            "average_read_time_in_seconds": 525,
            "total_read_time_in_seconds": 525
        }
    },
    "2023-08-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 10,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 0
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 2,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 30
        }
    },
    "2023-08-20": {
        "comments": {
            "total": 1
        },
        "follows": {
            "total": 2
        },
        "reactions": {
            "total": 5,
            "like": 2,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 78,
            "average_read_time_in_seconds": 124,
            "total_read_time_in_seconds": 9672
        }
    },
    "2023-08-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 10
        },
        "reactions": {
            "total": 2,
            "like": 0,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 48,
            "average_read_time_in_seconds": 153,
            "total_read_time_in_seconds": 7344
        }
    },
    "2023-08-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 11
        },
        "reactions": {
            "total": 5,
            "like": 3,
            "readinglist": 1,
            "unicorn": 1
        },
        "page_views": {
            "total": 27,
            "average_read_time_in_seconds": 49,
            "total_read_time_in_seconds": 1323
        }
    },
    "2023-08-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 13
        },
        "reactions": {
            "total": 2,
            "like": 1,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 8,
            "average_read_time_in_seconds": 68,
            "total_read_time_in_seconds": 544
        }
    },
    "2023-08-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 9
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 26,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 390
        }
    },
    "2023-08-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 5
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 3
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 14,
            "average_read_time_in_seconds": 86,
            "total_read_time_in_seconds": 1204
        }
    },
    "2023-08-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 2
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 10,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-08-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 9
        },
        "reactions": {
            "total": 7,
            "like": 0,
            "readinglist": 3,
            "unicorn": 2
        },
        "page_views": {
            "total": 82,
            "average_read_time_in_seconds": 58,
            "total_read_time_in_seconds": 4756
        }
    },
    "2023-08-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 8
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 64,
            "average_read_time_in_seconds": 173,
            "total_read_time_in_seconds": 11072
        }
    },
    "2023-08-30": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 8
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 13,
            "average_read_time_in_seconds": 45,
            "total_read_time_in_seconds": 585
        }
    },
    "2023-08-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 26
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 21,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 315
        }
    },
    "2023-09-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 17
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 27,
            "average_read_time_in_seconds": 184,
            "total_read_time_in_seconds": 4968
        }
    },
    "2023-09-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 12
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 0,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-09-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 18
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 30,
            "average_read_time_in_seconds": 0,
            "total_read_time_in_seconds": 0
        }
    },
    "2023-09-04": {
        "comments": {
            "total": 2
        },
        "follows": {
            "total": 34
        },
        "reactions": {
            "total": 1,
            "like": 1,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 19,
            "average_read_time_in_seconds": 28,
            "total_read_time_in_seconds": 532
        }
    },
    "2023-09-05": {
        "comments": {
            "total": 1
        },
        "follows": {
            "total": 56
        },
        "reactions": {
            "total": 26,
            "like": 12,
            "readinglist": 0,
            "unicorn": 3
        },
        "page_views": {
            "total": 111,
            "average_read_time_in_seconds": 60,
            "total_read_time_in_seconds": 6660
        }
    },
    "2023-09-06": {
        "comments": {
            "total": 2
        },
        "follows": {
            "total": 115
        },
        "reactions": {
            "total": 2,
            "like": 0,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 125,
            "average_read_time_in_seconds": 94,
            "total_read_time_in_seconds": 11750
        }
    },
    "2023-09-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 149
        },
        "reactions": {
            "total": 21,
            "like": 6,
            "readinglist": 3,
            "unicorn": 4
        },
        "page_views": {
            "total": 208,
            "average_read_time_in_seconds": 106,
            "total_read_time_in_seconds": 22048
        }
    },
    "2023-09-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 113
        },
        "reactions": {
            "total": 4,
            "like": 3,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 214,
            "average_read_time_in_seconds": 228,
            "total_read_time_in_seconds": 48792
        }
    },
    "2023-09-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 55
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 27,
            "average_read_time_in_seconds": 306,
            "total_read_time_in_seconds": 8262
        }
    },
    "2023-09-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 60
        },
        "reactions": {
            "total": 2,
            "like": 1,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 36,
            "average_read_time_in_seconds": 142,
            "total_read_time_in_seconds": 5112
        }
    },
    "2023-09-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 135
        },
        "reactions": {
            "total": 7,
            "like": 2,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 176,
            "average_read_time_in_seconds": 206,
            "total_read_time_in_seconds": 36256
        }
    },
    "2023-09-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 99
        },
        "reactions": {
            "total": 6,
            "like": 3,
            "readinglist": 3,
            "unicorn": 0
        },
        "page_views": {
            "total": 206,
            "average_read_time_in_seconds": 191,
            "total_read_time_in_seconds": 39346
        }
    },
    "2023-09-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 96
        },
        "reactions": {
            "total": 11,
            "like": 5,
            "readinglist": 4,
            "unicorn": 0
        },
        "page_views": {
            "total": 1095,
            "average_read_time_in_seconds": 191,
            "total_read_time_in_seconds": 209145
        }
    },
    "2023-09-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 82
        },
        "reactions": {
            "total": 3,
            "like": 0,
            "readinglist": 2,
            "unicorn": 1
        },
        "page_views": {
            "total": 681,
            "average_read_time_in_seconds": 204,
            "total_read_time_in_seconds": 138924
        }
    },
    "2023-09-15": {
        "comments": {
            "total": 3
        },
        "follows": {
            "total": 49
        },
        "reactions": {
            "total": 7,
            "like": 1,
            "readinglist": 4,
            "unicorn": 0
        },
        "page_views": {
            "total": 442,
            "average_read_time_in_seconds": 266,
            "total_read_time_in_seconds": 117572
        }
    },
    "2023-09-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 60
        },
        "reactions": {
            "total": 7,
            "like": 1,
            "readinglist": 2,
            "unicorn": 1
        },
        "page_views": {
            "total": 300,
            "average_read_time_in_seconds": 86,
            "total_read_time_in_seconds": 25800
        }
    },
    "2023-09-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 89
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 407,
            "average_read_time_in_seconds": 184,
            "total_read_time_in_seconds": 74888
        }
    },
    "2023-09-18": {
        "comments": {
            "total": 5
        },
        "follows": {
            "total": 65
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 307,
            "average_read_time_in_seconds": 278,
            "total_read_time_in_seconds": 85346
        }
    },
    "2023-09-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 45
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 231,
            "average_read_time_in_seconds": 50,
            "total_read_time_in_seconds": 11550
        }
    },
    "2023-09-20": {
        "comments": {
            "total": 1
        },
        "follows": {
            "total": 99
        },
        "reactions": {
            "total": 17,
            "like": 5,
            "readinglist": 6,
            "unicorn": 3
        },
        "page_views": {
            "total": 310,
            "average_read_time_in_seconds": 187,
            "total_read_time_in_seconds": 57970
        }
    },
    "2023-09-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 79
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 132,
            "average_read_time_in_seconds": 263,
            "total_read_time_in_seconds": 34716
        }
    },
    "2023-09-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 47
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 76,
            "average_read_time_in_seconds": 348,
            "total_read_time_in_seconds": 26448
        }
    },
    "2023-09-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 44
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 62,
            "average_read_time_in_seconds": 45,
            "total_read_time_in_seconds": 2790
        }
    },
    "2023-09-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 28
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 58,
            "average_read_time_in_seconds": 60,
            "total_read_time_in_seconds": 3480
        }
    },
    "2023-09-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 66
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 75,
            "average_read_time_in_seconds": 202,
            "total_read_time_in_seconds": 15150
        }
    },
    "2023-09-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 71
        },
        "reactions": {
            "total": 9,
            "like": 5,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 125,
            "average_read_time_in_seconds": 100,
            "total_read_time_in_seconds": 12500
        }
    },
    "2023-09-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 75
        },
        "reactions": {
            "total": 13,
            "like": 6,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 255,
            "average_read_time_in_seconds": 103,
            "total_read_time_in_seconds": 26265
        }
    },
    "2023-09-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 32
        },
        "reactions": {
            "total": 9,
            "like": 3,
            "readinglist": 2,
            "unicorn": 0
        },
        "page_views": {
            "total": 428,
            "average_read_time_in_seconds": 87,
            "total_read_time_in_seconds": 37236
        }
    },
    "2023-09-29": {
        "comments": {
            "total": 20
        },
        "follows": {
            "total": 80
        },
        "reactions": {
            "total": 43,
            "like": 16,
            "readinglist": 7,
            "unicorn": 7
        },
        "page_views": {
            "total": 1277,
            "average_read_time_in_seconds": 116,
            "total_read_time_in_seconds": 148132
        }
    },
    "2023-09-30": {
        "comments": {
            "total": 3
        },
        "follows": {
            "total": 56
        },
        "reactions": {
            "total": 5,
            "like": 2,
            "readinglist": 3,
            "unicorn": 0
        },
        "page_views": {
            "total": 201,
            "average_read_time_in_seconds": 116,
            "total_read_time_in_seconds": 23316
        }
    },
    "2023-10-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 49
        },
        "reactions": {
            "total": 7,
            "like": 2,
            "readinglist": 5,
            "unicorn": 0
        },
        "page_views": {
            "total": 502,
            "average_read_time_in_seconds": 172,
            "total_read_time_in_seconds": 86344
        }
    },
    "2023-10-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 49
        },
        "reactions": {
            "total": 3,
            "like": 1,
            "readinglist": 2,
            "unicorn": 0
        },
        "page_views": {
            "total": 312,
            "average_read_time_in_seconds": 104,
            "total_read_time_in_seconds": 32448
        }
    },
    "2023-10-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 77
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 432,
            "average_read_time_in_seconds": 109,
            "total_read_time_in_seconds": 47088
        }
    },
    "2023-10-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 85
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 418,
            "average_read_time_in_seconds": 209,
            "total_read_time_in_seconds": 87362
        }
    },
    "2023-10-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 23
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 232,
            "average_read_time_in_seconds": 233,
            "total_read_time_in_seconds": 54056
        }
    },
    "2023-10-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 10
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 195,
            "average_read_time_in_seconds": 777,
            "total_read_time_in_seconds": 151515
        }
    },
    "2023-10-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 23
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 104,
            "average_read_time_in_seconds": 137,
            "total_read_time_in_seconds": 14248
        }
    },
    "2023-10-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 6
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 55,
            "average_read_time_in_seconds": 39,
            "total_read_time_in_seconds": 2145
        }
    },
    "2023-10-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 36
        },
        "reactions": {
            "total": 8,
            "like": 2,
            "readinglist": 0,
            "unicorn": 2
        },
        "page_views": {
            "total": 254,
            "average_read_time_in_seconds": 48,
            "total_read_time_in_seconds": 12192
        }
    },
    "2023-10-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 62
        },
        "reactions": {
            "total": 5,
            "like": 2,
            "readinglist": 3,
            "unicorn": 0
        },
        "page_views": {
            "total": 323,
            "average_read_time_in_seconds": 240,
            "total_read_time_in_seconds": 77520
        }
    },
    "2023-10-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 47
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 300,
            "average_read_time_in_seconds": 259,
            "total_read_time_in_seconds": 77700
        }
    },
    "2023-10-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 67
        },
        "reactions": {
            "total": 10,
            "like": 2,
            "readinglist": 0,
            "unicorn": 2
        },
        "page_views": {
            "total": 150,
            "average_read_time_in_seconds": 210,
            "total_read_time_in_seconds": 31500
        }
    },
    "2023-10-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 61
        },
        "reactions": {
            "total": 2,
            "like": 1,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 378,
            "average_read_time_in_seconds": 84,
            "total_read_time_in_seconds": 31752
        }
    },
    "2023-10-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 49
        },
        "reactions": {
            "total": 1,
            "like": 1,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 119,
            "average_read_time_in_seconds": 203,
            "total_read_time_in_seconds": 24157
        }
    },
    "2023-10-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 32
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 88,
            "average_read_time_in_seconds": 258,
            "total_read_time_in_seconds": 22704
        }
    },
    "2023-10-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 64
        },
        "reactions": {
            "total": 10,
            "like": 4,
            "readinglist": 1,
            "unicorn": 2
        },
        "page_views": {
            "total": 217,
            "average_read_time_in_seconds": 188,
            "total_read_time_in_seconds": 40796
        }
    },
    "2023-10-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 117
        },
        "reactions": {
            "total": 5,
            "like": 2,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 170,
            "average_read_time_in_seconds": 99,
            "total_read_time_in_seconds": 16830
        }
    },
    "2023-10-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 35
        },
        "reactions": {
            "total": 3,
            "like": 1,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 153,
            "average_read_time_in_seconds": 73,
            "total_read_time_in_seconds": 11169
        }
    },
    "2023-10-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 50
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 333,
            "average_read_time_in_seconds": 147,
            "total_read_time_in_seconds": 48951
        }
    },
    "2023-10-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 57
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 238,
            "average_read_time_in_seconds": 61,
            "total_read_time_in_seconds": 14518
        }
    },
    "2023-10-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 52
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 144,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 2160
        }
    },
    "2023-10-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 17
        },
        "reactions": {
            "total": 1,
            "like": 0,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 121,
            "average_read_time_in_seconds": 327,
            "total_read_time_in_seconds": 39567
        }
    },
    "2023-10-23": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 59
        },
        "reactions": {
            "total": 5,
            "like": 3,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 242,
            "average_read_time_in_seconds": 43,
            "total_read_time_in_seconds": 10406
        }
    },
    "2023-10-24": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 28
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 67,
            "average_read_time_in_seconds": 43,
            "total_read_time_in_seconds": 2881
        }
    },
    "2023-10-25": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 37
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 112,
            "average_read_time_in_seconds": 34,
            "total_read_time_in_seconds": 3808
        }
    },
    "2023-10-26": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 44
        },
        "reactions": {
            "total": 6,
            "like": 2,
            "readinglist": 2,
            "unicorn": 0
        },
        "page_views": {
            "total": 221,
            "average_read_time_in_seconds": 292,
            "total_read_time_in_seconds": 64532
        }
    },
    "2023-10-27": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 22
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 171,
            "average_read_time_in_seconds": 439,
            "total_read_time_in_seconds": 75069
        }
    },
    "2023-10-28": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 9
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 249,
            "average_read_time_in_seconds": 107,
            "total_read_time_in_seconds": 26643
        }
    },
    "2023-10-29": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 34
        },
        "reactions": {
            "total": 14,
            "like": 4,
            "readinglist": 0,
            "unicorn": 3
        },
        "page_views": {
            "total": 205,
            "average_read_time_in_seconds": 70,
            "total_read_time_in_seconds": 14350
        }
    },
    "2023-10-30": {
        "comments": {
            "total": 2
        },
        "follows": {
            "total": 35
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 269,
            "average_read_time_in_seconds": 129,
            "total_read_time_in_seconds": 34701
        }
    },
    "2023-10-31": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 59
        },
        "reactions": {
            "total": 21,
            "like": 6,
            "readinglist": 6,
            "unicorn": 2
        },
        "page_views": {
            "total": 909,
            "average_read_time_in_seconds": 135,
            "total_read_time_in_seconds": 122715
        }
    },
    "2023-11-01": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 34
        },
        "reactions": {
            "total": 7,
            "like": 2,
            "readinglist": 1,
            "unicorn": 2
        },
        "page_views": {
            "total": 309,
            "average_read_time_in_seconds": 297,
            "total_read_time_in_seconds": 91773
        }
    },
    "2023-11-02": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 14
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 240,
            "average_read_time_in_seconds": 173,
            "total_read_time_in_seconds": 41520
        }
    },
    "2023-11-03": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 34
        },
        "reactions": {
            "total": 2,
            "like": 1,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 300,
            "average_read_time_in_seconds": 78,
            "total_read_time_in_seconds": 23400
        }
    },
    "2023-11-04": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 19
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 120,
            "average_read_time_in_seconds": 252,
            "total_read_time_in_seconds": 30240
        }
    },
    "2023-11-05": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 10
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 112,
            "average_read_time_in_seconds": 645,
            "total_read_time_in_seconds": 72240
        }
    },
    "2023-11-06": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 4
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 172,
            "average_read_time_in_seconds": 30,
            "total_read_time_in_seconds": 5160
        }
    },
    "2023-11-07": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 40
        },
        "reactions": {
            "total": 18,
            "like": 5,
            "readinglist": 0,
            "unicorn": 3
        },
        "page_views": {
            "total": 348,
            "average_read_time_in_seconds": 155,
            "total_read_time_in_seconds": 53940
        }
    },
    "2023-11-08": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 42
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 210,
            "average_read_time_in_seconds": 290,
            "total_read_time_in_seconds": 60900
        }
    },
    "2023-11-09": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 65
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 191,
            "average_read_time_in_seconds": 52,
            "total_read_time_in_seconds": 9932
        }
    },
    "2023-11-10": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 29
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 177,
            "average_read_time_in_seconds": 77,
            "total_read_time_in_seconds": 13629
        }
    },
    "2023-11-11": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 14
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 132,
            "average_read_time_in_seconds": 193,
            "total_read_time_in_seconds": 25476
        }
    },
    "2023-11-12": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 19
        },
        "reactions": {
            "total": 7,
            "like": 3,
            "readinglist": 0,
            "unicorn": 1
        },
        "page_views": {
            "total": 185,
            "average_read_time_in_seconds": 80,
            "total_read_time_in_seconds": 14800
        }
    },
    "2023-11-13": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 24
        },
        "reactions": {
            "total": 3,
            "like": 1,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 222,
            "average_read_time_in_seconds": 345,
            "total_read_time_in_seconds": 76590
        }
    },
    "2023-11-14": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 13
        },
        "reactions": {
            "total": 3,
            "like": 1,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 248,
            "average_read_time_in_seconds": 501,
            "total_read_time_in_seconds": 124248
        }
    },
    "2023-11-15": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 21
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 218,
            "average_read_time_in_seconds": 514,
            "total_read_time_in_seconds": 112052
        }
    },
    "2023-11-16": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 47
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 185,
            "average_read_time_in_seconds": 42,
            "total_read_time_in_seconds": 7770
        }
    },
    "2023-11-17": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 28
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 201,
            "average_read_time_in_seconds": 239,
            "total_read_time_in_seconds": 48039
        }
    },
    "2023-11-18": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 13
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 82,
            "average_read_time_in_seconds": 15,
            "total_read_time_in_seconds": 1230
        }
    },
    "2023-11-19": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 10
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 55,
            "average_read_time_in_seconds": 402,
            "total_read_time_in_seconds": 22110
        }
    },
    "2023-11-20": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 31
        },
        "reactions": {
            "total": 16,
            "like": 4,
            "readinglist": 1,
            "unicorn": 2
        },
        "page_views": {
            "total": 241,
            "average_read_time_in_seconds": 129,
            "total_read_time_in_seconds": 31089
        }
    },
    "2023-11-21": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 40
        },
        "reactions": {
            "total": 0,
            "like": 0,
            "readinglist": 0,
            "unicorn": 0
        },
        "page_views": {
            "total": 274,
            "average_read_time_in_seconds": 238,
            "total_read_time_in_seconds": 65212
        }
    },
    "2023-11-22": {
        "comments": {
            "total": 0
        },
        "follows": {
            "total": 20
        },
        "reactions": {
            "total": 8,
            "like": 3,
            "readinglist": 1,
            "unicorn": 0
        },
        "page_views": {
            "total": 96,
            "average_read_time_in_seconds": 40,
            "total_read_time_in_seconds": 3840
        }
    }
}

data = []
for date, metrics in input.items():
    for metric, values in metrics.items():
        for key, value in values.items():
            data.append([date, metric, key, value])

df = pd.DataFrame(data, columns=['Date', 'Metric', 'Key', 'Value'])

# Now you can filter and reshape your DataFrame as needed
df_follows = df[(df['Metric'] == 'follows') & (df['Key'] == 'total')]
df_follows.columns = ['Date', 'Metric', 'Key', 'Followers']

# Print to console in CSV format
print(df_follows.to_csv(index=False))