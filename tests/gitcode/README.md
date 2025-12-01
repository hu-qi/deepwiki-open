# GitCode API v5 Testing Guide

This directory contains tests for the GitCode API v5 integration in DeepWiki.

## Test Files

### 1. `test_gitcode_url_extraction.py` (Recommended)

**Lightweight standalone test** that doesn't require any external dependencies beyond Python standard library.

```bash
# Run the test
python test/test_gitcode_url_extraction.py
```

**Coverage:**

- ✅ GitCode repository name extraction from URLs
- ✅ Support for .git suffix and trailing slashes
- ✅ Subgroup URL handling
- ✅ GitCode API v5 endpoint construction
- ✅ Bearer token authentication validation
- ✅ GitCode vs GitLab API difference documentation

**Output:**

```
======================================================================
GitCode URL Extraction & API Test Suite
======================================================================

Repository Name Extraction Tests:
----------------------------------------------------------------------
✓ GitCode standard URL
✓ GitCode URL with .git suffix
✓ GitCode URL with trailing slash
✓ GitCode URL with subgroups
✓ GitCode .net domain
✓ GitCode vs GitLab URL extraction

GitCode API v5 Endpoint Tests:
----------------------------------------------------------------------
✓ API endpoint construction
✓ Bearer token authentication
✓ GitCode vs GitLab API differences

======================================================================
Test Summary: 9/9 passed
✅ All tests passed!
======================================================================
```

### 2. `test_gitcode_api.py` (Full Test Suite)

**Comprehensive test suite** with pytest support and mock testing for API calls.

```bash
# Run with pytest (if installed)
pytest test/test_gitcode_api.py -v

# Or run directly
python test/test_gitcode_api.py
```

**Note:** Requires `adalflow` and other project dependencies to be installed.

**Coverage:**

- Repository name extraction
- API URL construction
- Authentication headers
- File content retrieval (mocked)
- Error handling (401, 404, 429)
- GitCode vs GitLab differences

### 3. `test_extract_repo_name.py` (Existing)

General repository name extraction tests for GitHub, GitLab, Bitbucket, and local paths.

## GitCode API v5 Key Features Tested

### API Endpoints

```python
# Repository Info
https://api.gitcode.com/api/v5/repos/{owner}/{repo}

# File Tree (recursive)
https://api.gitcode.com/api/v5/repos/{owner}/{repo}/git/trees/{branch}?recursive=1

# File Content
https://api.gitcode.com/api/v5/repos/{owner}/{repo}/contents/{path}
```

### Authentication

```python
headers = {
    "Authorization": "Bearer {token}",
    "Content-Type": "application/json"
}
```

### Differences from GitLab API

| Feature            | GitCode v5                        | GitLab v4                         |
| ------------------ | --------------------------------- | --------------------------------- |
| **API Version**    | `/api/v5/`                        | `/api/v4/`                        |
| **Base Domain**    | `api.gitcode.com`                 | `gitlab.com`                      |
| **Authentication** | `Authorization: Bearer {token}`   | `PRIVATE-TOKEN: {token}`          |
| **Repo Endpoint**  | `/repos/{owner}/{repo}`           | `/projects/{encoded_path}`        |
| **Tree Endpoint**  | `/git/trees/{branch}?recursive=1` | `/repository/tree?recursive=true` |
| **File Content**   | Base64 encoded (like GitHub)      | Raw text by default               |
| **Pagination**     | Not needed with `recursive=1`     | Required for large repos          |

## Running All Tests

To run all tests in the test directory:

```bash
# Run all tests with Python
for test_file in test/test_*.py; do
    echo "Running $test_file"
    python "$test_file"
    echo ""
done
```

## Implementation Reference

The GitCode API v5 implementation can be found in:

- **Frontend:** `src/app/[owner]/[repo]/page.tsx` (lines 164-175, 1419-1485)
- **Backend:** `api/data_pipeline.py` (line 112, line 766)

## Continuous Integration

To add these tests to CI/CD:

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.9"
      - name: Run GitCode URL extraction tests
        run: python test/test_gitcode_url_extraction.py
```

## Contributing

When adding new GitCode API functionality, please:

1. Add corresponding tests to `test_gitcode_api.py`
2. Update this documentation
3. Ensure all tests pass before submitting PR

## References

- [GitCode API Documentation](https://docs.gitcode.com/docs/apis/)
- [GitCode API v5 Endpoints](https://docs.gitcode.com/docs/apis/get-api-v-5-repos-owner-repo-git-trees-sha)
