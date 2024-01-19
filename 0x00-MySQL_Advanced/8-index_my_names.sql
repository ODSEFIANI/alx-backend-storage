-- indexing the first leter of names

CREATE INDEX idx_name_first ON names(name(1))