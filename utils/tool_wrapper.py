def safe_tool_execution(tool, args):

    try:
        return tool.invoke(args)

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }