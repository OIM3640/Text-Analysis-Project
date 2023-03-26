from imdb import Cinemagoer
import torch


def find_movie_review(ia, movie_id):
    movie_reviews = ia.get_movie_reviews(movie_id)
    review_1 = movie_reviews['data']['reviews'][1]['content']
    review_2 = movie_reviews['data']['reviews'][2]['content']
    return review_1, review_2


def main():
    # create an instance of the Cinemagoer class
    ia = Cinemagoer()

    # search movie
    movie = ia.search_movie("Up")[0]
    movie_id = movie.getID()

    # find movie reviews
    review_1, review_2 = find_movie_review(ia, movie_id)

    # print movie reviews
    print(f"Review 1:\n{review_1}\n\nReview 2:\n{review_2}")

    # similarity
    from thefuzz import fuzz
    from thefuzz import process
    # print(fuzz.ratio(review_1,review_2))

    # text generation using GPT-2 model
    # import libraries
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

    # load imports
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    # defining a prompt
    prompt = """This film is possibly one of the best animated films of all time as it tells an emotional moving story while being funny. 
    As I said the emotion in this film is full of heart and even though I didnt cry it will make most people cry."""

    # encoded prompt
    inputs = tokenizer(prompt, return_tensors='pt')

    # create attention mask
    input_ids = inputs['input_ids']
    attention_mask = torch.ones_like(input_ids)
    padding_mask = input_ids == tokenizer.pad_token_id
    attention_mask[padding_mask] = 0

    # generate text from model
    outputs = model.generate(
        inputs['input_ids'], attention_mask=attention_mask, max_length=1000, do_sample=True)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f'Generated text:\n {generated_text}')


if __name__ == "__main__":
    main()
