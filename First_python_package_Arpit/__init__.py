from preprocess_20201109 import utils

__version__ = '0.0.1'

def get_word_counts(x):
	return utils._get_word_counts(x)

def get_char_counts(x):
	return utils._get_char_counts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hashtag_count(x):
	return utils._get_hashtag_count(x)

def get_mention_count(x):
	return utils._get_mention_count(x)

def get_digit_count(x):
	return utils._get_digit_count(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def get_cont_exp(x):
	return utils._get_cont_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)

def remove_spacial_chars(x):
	return utils._remove_spacial_chars(x)

def remove_html_tag(x):
	return utils._remove_html_tag(x)

def remove_accented_char(x):
	return utils._remove_accented_char(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_to_base(x):
	return utils._make_to_base(x)

def remove_common_words(x):
	return utils._remove_common_words(x)

def remove_rare_words(x):
	return utils._remove_rare_words(x)

def spelling_correction(x):
	return utils._spelling_correction(x)

