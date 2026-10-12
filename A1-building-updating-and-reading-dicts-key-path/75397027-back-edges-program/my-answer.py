# Code from my Stack Overflow answer https://stackoverflow.com/a/75404626 (posted 2023-02-09), extracted verbatim; may need the question's context to run.
def ArcA(graph, start):
    stack = []
    discovery_time = {}
    finish_time = {}
    back_edges = []
    time = 0

    stack.append(start)

    while stack:
        current = stack.pop()
        if current not in discovery_time:
            time += 1
            discovery_time[current] = time
            stack.append(current)

            for neighbor in graph[current]:
                if neighbor not in discovery_time:
                    stack.append(neighbor)
                elif neighbor in stack: ### EDIT ###
                    back_edges.append((current, neighbor))

            time += 1
            finish_time[current] = time

    return back_edges
