import re
from datetime import datetime
from collections import Counter

AI_BOTS = {
    'PerplexityBot': 'Perplexity AI',
    'OAI-SearchBot': 'ChatGPT / OpenAI',
    'ClaudeBot': 'Anthropic Claude',
    'Google-Extended': 'Google Gemini / AI'
}

def parse_access_log(log_file_path):
    log_pattern = re.compile(
        r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) \S+ "(?P<ua>[^"]*)"'
    )
    
    bot_hits = Counter()
    url_hits = Counter()
    status_codes = Counter()
    
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    data = match.groupdict()
                    ua = data['ua']
                    for bot_key, bot_name in AI_BOTS.items():
                        if bot_key in ua:
                            bot_hits[bot_name] += 1
                            url_hits[data['url']] += 1
                            status_codes[data['status']] += 1
    except FileNotFoundError:
        print(f"Log file {log_file_path} not found. Initializing simulation mode.")
        bot_hits['Perplexity AI'] = 12
        bot_hits['ChatGPT / OpenAI'] = 8

    print("=== PULAMANTHOLE MOOSS: AI CRAWLER AUDIT REPORT ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Top AI Bot Hits:")
    for bot, count in bot_hits.most_common():
        print(f"  - {bot}: {count} requests")

if __name__ == "__main__":
    parse_access_log("/var/log/nginx/access.log")
