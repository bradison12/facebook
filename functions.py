from transformers import AutoTokenizer
import openai
import csv
openai.api_key = "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"


class AIsearcher:
    response = ''
    prompt = ''
    model_engine = 'text-davinci-003'

    def __init__(self):
        pass

    async def update_response_text(self):
        tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')
        count = 4096 - len(tokenizer.encode("".join(self.prompt)))
        self.response = openai.Completion.create(
            model=self.model_engine, prompt=self.prompt, temperature=0, max_tokens=count
        )
        del tokenizer
        del count

    async def get_prompt_response_text(self):
        with open('text_for_post.csv', 'r+', newline='') as file:
            reader = csv.reader(file)
            first_row = next(reader)
            lines = [line for line in reader]
            file.seek(0)
            writer = csv.writer(file)
            writer.writerows(lines)
            file.truncate()
        self.prompt = first_row
        await self.update_response_text()
