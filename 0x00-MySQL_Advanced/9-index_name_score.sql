-- indexing the first leter of names and score

CREATE INDEX idx_name_first ON names(name(1), score)