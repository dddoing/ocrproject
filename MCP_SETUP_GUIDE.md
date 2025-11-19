# MCP Server Setup Guide

This guide will help you set up the three MCP servers for the Universal Document Translator project.

## Prerequisites

- Node.js 18+ installed
- Claude Code CLI installed
- Docker installed (for PostgreSQL)
- GitHub account with repository access

## Step 1: Set Up PostgreSQL Database

First, let's start the PostgreSQL database using Docker:

```bash
# Start PostgreSQL container
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 \
  -d postgres:15

# Verify it's running
docker ps | grep doc-translator-db

# Optional: Connect to verify
docker exec -it doc-translator-db psql -U docuser -d docdb
# Type \q to exit
```

## Step 2: Create GitHub Personal Access Token

1. Go to GitHub: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Universal Document Translator MCP"
4. Select the following scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
   - ✅ `read:user` (Read user profile data)
5. Click "Generate token"
6. **Copy the token immediately** (you won't be able to see it again)

## Step 3: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env

# Edit with your values
nano .env  # or use your preferred editor
```

Add your credentials to `.env`:

```bash
# PostgreSQL Database
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb

# GitHub Token
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_actual_token_here

# Claude API (for the application)
ANTHROPIC_API_KEY=your_claude_api_key_here
```

Then export them to your shell:

```bash
# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Or on macOS/Linux, add to your shell profile (~/.zshrc or ~/.bashrc):
echo 'export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token' >> ~/.zshrc
echo 'export DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb' >> ~/.zshrc
source ~/.zshrc
```

## Step 4: Verify MCP Configuration

The `.mcp.json` file has already been created. Verify it exists:

```bash
cat .mcp.json
```

You should see the configuration for all three servers:
- ✅ GitHub MCP Server
- ✅ Filesystem MCP Server
- ✅ PostgreSQL MCP Server

## Step 5: Test MCP Servers

Once you've set up the environment variables, Claude Code will automatically use the MCP servers. You can verify them:

```bash
# List all configured MCP servers
claude mcp list

# Get details about a specific server
claude mcp get github
claude mcp get filesystem
claude mcp get postgresql
```

## Step 6: Verify in Claude Code

1. Open Claude Code in your project directory
2. Type `/mcp` to see the status of all MCP servers
3. You should see all three servers listed as available

## Using the MCP Servers

### GitHub MCP Server

You can now ask Claude Code to:
- Create pull requests
- Read issues and comments
- Manage branches
- View repository information

Example commands:
```
"Show me all open issues in this repository"
"Create a new branch called feature/ocr-service"
"Create a PR for the current changes"
```

### Filesystem MCP Server

Enhanced file operations:
```
"List all Python files in the backend directory"
"Show me the directory structure"
"Find all files containing 'OCR'"
```

### PostgreSQL MCP Server

Database queries and management:
```
"Show me all tables in the database"
"Query the user history table"
"Create an index on the documents table"
```

## Troubleshooting

### MCP Servers Not Showing Up

1. Check environment variables are set:
   ```bash
   echo $GITHUB_PERSONAL_ACCESS_TOKEN
   echo $DATABASE_URL
   ```

2. Verify PostgreSQL is running:
   ```bash
   docker ps | grep doc-translator-db
   ```

3. Test database connection:
   ```bash
   psql $DATABASE_URL -c "SELECT version();"
   ```

### GitHub Token Issues

- Make sure the token has the correct scopes (`repo`, `workflow`, `read:user`)
- Token should start with `ghp_` (classic token)
- Check token hasn't expired

### PostgreSQL Connection Issues

- Verify Docker container is running
- Check port 5432 isn't in use by another process:
  ```bash
  lsof -i :5432
  ```
- Try connecting directly:
  ```bash
  docker exec -it doc-translator-db psql -U docuser -d docdb
  ```

## Security Notes

- ✅ `.env` file is in `.gitignore` - never commit it
- ✅ `.mcp.json` uses environment variable references - safe to commit
- ✅ Rotate GitHub tokens periodically
- ✅ Use read-only database credentials when possible

## Next Steps

1. Initialize a git repository (if not already done):
   ```bash
   git init
   ```

2. Create your GitHub repository and connect it

3. Start building the backend and frontend:
   ```bash
   # Follow the setup instructions in CLAUDE.md
   ```

4. Use Claude Code to help develop the project with full MCP capabilities!

## Additional Resources

- [MCP Documentation](https://code.claude.com/docs/en/mcp)
- [GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- [PostgreSQL MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)
- [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
