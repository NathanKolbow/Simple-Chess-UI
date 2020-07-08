import PySimpleGUI as sg
import board_utils as butil

starting_pos_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def run():
	board = [
		[
			sg.Graph(canvas_size=(800, 800),
					graph_bottom_left=(0,0),
					graph_top_right=(800,800),
					key = "board"
			)
		]
	]

	printout = [
		[sg.Output(size=(100,20))],
	]

	layout = [
		[sg.Column(board)],
	]
	window = sg.Window('Match Analyzer', layout)

	board_graph = window.Element('board')
	window.Finalize()

	butil.Init(board_graph)


	#fen_data = butil.data_from_fen(starting_pos_fen)
	#butil.draw_from_data(board_graph, fen_data)
	butil.set_pos_from_fen(starting_pos_fen)



	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			break

	window.close()

if __name__ == '__main__':
	run()