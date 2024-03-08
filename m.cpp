#include <iostream>
#include <dpp/dpp.h>

using namespace std;

int main() {
	dpp::cluster bot(std::getenv("BOT_TOKEN"));

	bot.on_ready([&bot](auto event) {
		if (dpp::run_once<struct register_bot_commands>()) {
			bot.global_command_create(
				dpp::slashcommand("ping", "Ping pong!", bot.me.id)
			);
		}
	});

	bot.start(dpp::st_wait);
	return 0;
}