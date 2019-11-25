class Scoreboard:
    def __init__(self, num_results=1, variables=tuple(), lowest_score=0):
        self.ranking = [lowest_score] * num_results
        self.meta = [[key] * num_results for key in variables]

    def score_to_beat(self):
        return self.ranking[-1]

    def get_size(self):
        return len(self.ranking)

    def get_rankings(self):
        return self.ranking

    def get_meta(self):
        return self.meta

    def insert_into_ranking(self, score):
        index = self.get_size()
        for another_index, ranking in enumerate(self.ranking):
            if score > ranking:
                if another_index < index:
                    index = another_index
                score, self.ranking[another_index] = self.ranking[another_index], score
        return index

    def update_meta(self, meta_index, index, value):
        if len(value):
            self.meta[meta_index][index+1:] = self.meta[meta_index][index:]
            self.meta[meta_index][index] = value

    def update(self, scores, tup=tuple()):
        if tup:
            tup = list(zip(*tup))
        for i in range(len(scores)):
            score = scores[i]
            if tup:
                meta = tup[i]
            if score > self.score_to_beat():
                index = self.insert_into_ranking(score)
                for meta_index in range(len(self.meta)):
                    self.update_meta(meta_index, index, meta[meta_index])

    def top_score(self):
        return self.ranking[0]

    def top_meta(self):
        return [iterable[0] for iterable in self.meta]

    def __str__(self):
        output = "\n"
        for index, ranking in enumerate(self.ranking):
            output += "| Score: " + str(ranking) + "\n"
            for another_index, topic in enumerate(self.meta):
                output += "| Data Point (" + str(another_index) + "): "
                output += str(self.meta[another_index][index]) + "\n"
            output += "------------\n"
        return output
