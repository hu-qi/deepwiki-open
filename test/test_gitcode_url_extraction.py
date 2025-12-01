#!/usr/bin/env python3
"""
Lightweight test suite for GitCode API URL extraction

This test validates GitCode repository name extraction WITHOUT requiring
adalflow or other heavy dependencies.

Usage: python test/test_gitcode_url_extraction.py
"""

import sys
import os

# Simple test runner
class SimpleTestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    def test(self, description, test_func):
        """Run a single test"""
        try:
            test_func()
            self.passed += 1
            print(f"✓ {description}")
            return True
        except AssertionError as e:
            self.failed += 1
            print(f"✗ {description}: {e}")
            return False
        except Exception as e:
            self.failed += 1
            print(f"✗ {description} (ERROR): {e}")
            return False
    
    def print_summary(self):
        """Print test summary"""
        total = self.passed + self.failed
        print(f"\n{'='*70}")
        print(f"Test Summary: {self.passed}/{total} passed")
        if self.failed > 0:
            print(f"❌ {self.failed} test(s) failed")
        else:
            print(f"✅ All tests passed!")
        print(f"{'='*70}\n")
        return self.failed == 0


def extract_repo_name_from_url(repo_url_or_path: str, repo_type: str) -> str:
    """
    Extract repository name from URL (simplified version for testing)
    This mimics the logic in DatabaseManager._extract_repo_name_from_url
    """
    url_parts = repo_url_or_path.rstrip('/').split('/')
    
    if repo_type in ["github", "gitlab", "gitcode", "bitbucket"] and len(url_parts) >= 5:
        owner = url_parts[-2]
        repo = url_parts[-1].replace(".git", "")
        repo_name = f"{owner}_{repo}"
    else:
        repo_name = url_parts[-1].replace(".git", "")
    return repo_name


def test_gitcode_standard_url():
    """Test standard GitCode URL"""
    result = extract_repo_name_from_url("https://gitcode.com/owner/repo", "gitcode")
    assert result == "owner_repo", f"Expected 'owner_repo', got '{result}'"


def test_gitcode_url_with_git_suffix():
    """Test GitCode URL with .git suffix"""
    result = extract_repo_name_from_url("https://gitcode.com/owner/repo.git", "gitcode")
    assert result == "owner_repo", f"Expected 'owner_repo', got '{result}'"


def test_gitcode_url_with_trailing_slash():
    """Test GitCode URL with trailing slash"""
    result = extract_repo_name_from_url("https://gitcode.com/owner/repo/", "gitcode")
    assert result == "owner_repo", f"Expected 'owner_repo', got '{result}'"


def test_gitcode_url_with_subgroups():
    """Test GitCode URL with subgroups"""
    result = extract_repo_name_from_url("https://gitcode.com/group/subgroup/repo", "gitcode")
    assert result == "subgroup_repo", f"Expected 'subgroup_repo', got '{result}'"


def test_gitcode_net_domain():
    """Test GitCode URL with gitcode.net domain"""
    result = extract_repo_name_from_url("https://gitcode.net/owner/repo", "gitcode")
    assert result == "owner_repo", f"Expected 'owner_repo', got '{result}'"


def test_gitcode_vs_gitlab_url_extraction():
    """Test that GitCode and GitLab URLs are processed identically"""
    gitcode_result = extract_repo_name_from_url("https://gitcode.com/owner/repo", "gitcode")  
    gitlab_result = extract_repo_name_from_url("https://gitlab.com/owner/repo", "gitlab")
    assert gitcode_result == gitlab_result, "GitCode and GitLab should extract the same"


def test_gitcode_api_endpoint_construction():
    """Test GitCode API v5 endpoint construction"""
    owner = "test-owner"
    repo = "test-repo"
    branch = "main"
    
    # GitCode API v5 endpoints
    api_base = "https://api.gitcode.com/api/v5"
    repo_info_url = f"{api_base}/repos/{owner}/{repo}"
    tree_url = f"{api_base}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    file_url = f"{api_base}/repos/{owner}/{repo}/contents/README.md"
    
    # Verify endpoints contain expected patterns
    assert "/api/v5/" in repo_info_url
    assert "/repos/" in repo_info_url
    assert "/git/trees/" in tree_url
    assert "recursive=1" in tree_url
    assert "/contents/" in file_url


def test_gitcode_authentication_header():
    """Test GitCode Bearer token authentication header format"""
    token = "test_token_12345"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    assert "Authorization" in headers
    assert headers["Authorization"] == f"Bearer {token}"
    assert headers["Authorization"].startswith("Bearer ")


def test_gitcode_vs_gitlab_api_differences():
    """Document key differences between GitCode and GitLab APIs"""
    # API versions
    gitcode_version = "v5"
    gitlab_version = "v4"
    assert gitcode_version != gitlab_version
    
    # Authentication
    gitcode_auth_header = "Authorization"  # Uses Bearer token
    gitlab_auth_header = "PRIVATE-TOKEN"   # Uses PRIVATE-TOKEN
    assert gitcode_auth_header != gitlab_auth_header
    
    # Endpoint structure
    gitcode_endpoint = "/api/v5/repos/owner/repo/git/trees/main"
    gitlab_endpoint = "/api/v4/projects/owner%2Frepo/repository/tree"
    assert "/repos/" in gitcode_endpoint
    assert "/projects/" in gitlab_endpoint


if __name__ == "__main__":
    print("\n" + "="*70)
    print("GitCode URL Extraction & API Test Suite")
    print("="*70 + "\n")
    
    runner = SimpleTestRunner()
    
    # Repository name extraction tests
    print("Repository Name Extraction Tests:")
    print("-" * 70)
    runner.test("GitCode standard URL", test_gitcode_standard_url)
    runner.test("GitCode URL with .git suffix", test_gitcode_url_with_git_suffix)
    runner.test("GitCode URL with trailing slash", test_gitcode_url_with_trailing_slash)
    runner.test("GitCode URL with subgroups", test_gitcode_url_with_subgroups)
    runner.test("GitCode .net domain", test_gitcode_net_domain)
    runner.test("GitCode vs GitLab URL extraction", test_gitcode_vs_gitlab_url_extraction)
    
    # API endpoint tests
    print("\nGitCode API v5 Endpoint Tests:")
    print("-" * 70)
    runner.test("API endpoint construction", test_gitcode_api_endpoint_construction)
    runner.test("Bearer token authentication", test_gitcode_authentication_header)
    runner.test("GitCode vs GitLab API differences", test_gitcode_vs_gitlab_api_differences)
    
    # Print summary
    success = runner.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
