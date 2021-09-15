class NerModelTestDouble:
    """
    Test double for spaCy NPL model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)


class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label']) for ent in ents]

    def patch_method(self, attr, return_value):
        def pactched(): return return_value
        setattr(self, attr, pactched)
        return self


class SpanTestDouble:
    """
    Test double for spaCy Span
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label
