class Scoreboard:
    def __init__(self, num_results=1, variables=tuple(), lowest_score=0):
        self.ranking = [lowest_score] * num_results
        self.meta = [[key] * num_results for key in variables]

    def score_to_beat(self):
        return self.ranking[-1]

    def get_size(self):
        return len(self.ranking)

    def insert_into_ranking(self, score):
        index = self.get_size()
        for aIndex, aRanking in enumerate(self.ranking):
            if score > aRanking:
                if aIndex < index:
                    index = aIndex
                score, self.ranking[aIndex] = self.ranking[aIndex], score
        return index

    def update_meta(self, meta_index, index, iterable):
        if len(iterable):
            for anotherIndex, aRanking in enumerate(self.meta[meta_index]):
                if anotherIndex >= index:
                    self.meta[meta_index][anotherIndex] = iterable[meta_index]
                    iterable[meta_index] = aRanking

    def update(self, score, tup=tuple()):
        if score > self.score_to_beat():
            index = self.insert_into_ranking(score)
            for meta_index in range(len(self.meta)):
                self.update_meta(meta_index, index, list(tup))

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
