import argparse
import Logic 

def call_add(args, logic):
    logic.add_task(description=args.description)

def call_update(args, logic):
    logic.update_task(ID=args.ID, description=args.description)

def call_delete(args, logic):
    logic.delete_task(ID=args.ID)

def call_mark(args, logic):
    logic.mark_task(ID=args.ID, status=args.command)

def call_list(args, logic):
    logic.list_task(status=args.status)

def main():
    # Main parser
    parser = argparse.ArgumentParser(
        description="An app that help you keep track your works"
        )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description', type=str)
    add_parser.set_defaults(func=call_add)
    
    # 'update' command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('ID', type=int)
    update_parser.add_argument('description', type=str)
    update_parser.set_defaults(func=call_update)

    # 'delete' command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('ID', type=int)
    delete_parser.set_defaults(func=call_delete)

    # 'Marking' command 
    progress_parser = subparsers.add_parser('mark-in-progress')
    progress_parser.add_argument('ID', type=int)
    progress_parser.set_defaults(func=call_mark)

    done_parser = subparsers.add_parser('mark-done')
    done_parser.add_argument('ID', type=int)
    done_parser.set_defaults(func=call_mark)

    # 'List' command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('status', nargs='?', 
                        choices=['todo', 'in-progress', 'done']
                        )
    list_parser.set_defaults(func=call_list)
    
    logic = Logic.Operation()
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args, logic)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()