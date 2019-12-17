class Abalone:
    def __init__(self, row):
        self.attributes = {
            "sex": row[0],
            "length": row[1],
            "diameter": row[2],
            "height": row[3],
            "wholeWeight": row[4],
            "shuckedWeight": row[5],
            "visceraWeight": row[6],
            "shellWeight": row[7],
            "rings": row[8]
        }

