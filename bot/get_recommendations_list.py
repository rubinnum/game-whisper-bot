from openai import OpenAI

import constants

client = OpenAI(organization=constants.ORGANIZATION_ID,
                project=constants.PROJECT_ID,
                api_key=constants.OPENAI_API_KEY)


def get_recommended_games(preferences):
    boilerplate_content = ('Based on the array of video games that I will provide you with, recommend me five video '
                           'games that I might like (only names, no explanation) divided with a coma\n')

    response = client.chat.completions.create(
        model=constants.GPT_MODEL,
        messages=[
            {'role': 'user', 'content': boilerplate_content + str(preferences)}
        ]
    )
    assistant_response = response.choices[0].message.content.strip()
    recommendation_list = assistant_response.split(', ')
    return recommendation_list


def output_recommended_games(preferences):
    recommended_games = get_recommended_games(preferences)
    print('Here is the list of recommended games: ')
    for i in range(len(recommended_games)):
        print(f'{i + 1}. {recommended_games[i]}')


if __name__ == '__main__':
    preferences = input('Enter your favourite games (separate by comma and space): ').split(', ')
    output_recommended_games(preferences)
